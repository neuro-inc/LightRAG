#!/usr/bin/env python3
"""
LightRAG Storage Setup Script

This script helps you choose and configure different storage backends for LightRAG.
"""

import os
import sys
import shutil
import subprocess
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_section(title):
    """Print a formatted section header."""
    print(f"\n🔧 {title}")
    print("-" * 40)

def run_command(command, description):
    """Run a shell command and return success status."""
    print(f"Running: {description}")
    print(f"Command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print("✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def wait_for_service(service_name, host, port, timeout=60):
    """Wait for a service to be ready."""
    print(f"⏳ Waiting for {service_name} to be ready...")
    import socket
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"✅ {service_name} is ready!")
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            time.sleep(2)
            print(".", end="", flush=True)
    
    print(f"\n❌ {service_name} failed to start within {timeout} seconds")
    return False

def choose_storage_backend():
    """Let user choose storage backend configuration."""
    print_section("Storage Backend Selection")
    
    options = {
        "1": {
            "name": "Default Local Storage",
            "description": "File-based storage (NetworkX + NanoVectorDB + JSON)",
            "config": ".env.default",
            "compose": "docker-compose.yml",
            "deps": []
        },
        "2": {
            "name": "PostgreSQL + pgvector",
            "description": "PostgreSQL for all storage (graph, vectors, KV)",
            "config": ".env.postgres",
            "compose": "docker-compose.full.yml", 
            "deps": ["postgres"]
        },
        "3": {
            "name": "Neo4j + Qdrant + Redis",
            "description": "Specialized databases (Neo4j graph, Qdrant vectors, Redis KV)",
            "config": ".env.neo4j",
            "compose": "docker-compose.full.yml",
            "deps": ["neo4j", "qdrant", "redis"]
        },
        "4": {
            "name": "Full Stack",
            "description": "All databases available (for testing different backends)",
            "config": ".env.postgres",  # Default to postgres
            "compose": "docker-compose.full.yml",
            "deps": ["postgres", "neo4j", "qdrant", "redis", "etcd", "minio", "milvus-standalone", "chromadb", "mongodb"]
        }
    }
    
    print("Available storage configurations:")
    for key, option in options.items():
        print(f"  {key}. {option['name']}")
        print(f"     {option['description']}")
    
    while True:
        choice = input("\nSelect configuration (1-4): ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice. Please select 1-4.")

def setup_environment_file(config_template):
    """Setup the .env file from template."""
    print_section("Environment Configuration")
    
    if not os.path.exists(config_template):
        print(f"❌ Template {config_template} not found!")
        return False
    
    # Check if .env already exists
    if os.path.exists(".env"):
        response = input(".env file already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print("Keeping existing .env file...")
            return True
    
    # Copy template to .env
    shutil.copy(config_template, ".env")
    print(f"✅ Copied {config_template} to .env")
    
    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n⚠️  OpenAI API Key required!")
        api_key = input("Enter your OpenAI API key: ").strip()
        if api_key:
            # Update .env file
            with open(".env", "r") as f:
                content = f.read()
            
            content = content.replace("your_api_key", api_key)
            
            with open(".env", "w") as f:
                f.write(content)
            
            print("✅ Updated .env with API key")
        else:
            print("❌ No API key provided. You'll need to update .env manually.")
            return False
    
    return True

def start_services(compose_file, dependencies):
    """Start Docker services."""
    print_section("Starting Docker Services")
    
    if not os.path.exists(compose_file):
        print(f"❌ Docker compose file {compose_file} not found!")
        return False
    
    # Stop any existing services
    print("Stopping existing services...")
    run_command(f"docker-compose -f {compose_file} down", "Stop existing services")
    
    # Start services
    if dependencies:
        # Start dependencies first
        deps_str = " ".join(dependencies)
        if not run_command(f"docker-compose -f {compose_file} up -d {deps_str}", 
                          f"Start dependencies: {deps_str}"):
            return False
        
        # Wait for key services
        service_checks = {
            "postgres": ("localhost", 5432),
            "neo4j": ("localhost", 7475),
            "redis": ("localhost", 6380),
            "qdrant": ("localhost", 6333),
            "milvus-standalone": ("localhost", 19530),
            "chromadb": ("localhost", 8001),
            "mongodb": ("localhost", 27017),
        }
        
        for dep in dependencies:
            if dep in service_checks:
                host, port = service_checks[dep]
                if not wait_for_service(dep, host, port):
                    print(f"⚠️  {dep} might not be ready, but continuing...")
        
        # Now start LightRAG
        time.sleep(5)  # Give databases a moment to fully initialize
    
    # Start LightRAG service
    success = run_command(f"docker-compose -f {compose_file} up -d lightrag", 
                         "Start LightRAG service")
    
    if success:
        print("\n✅ Services started successfully!")
        print("LightRAG will be available at: http://localhost:9621")
        
        # Show running services
        print("\n📋 Running services:")
        subprocess.run(f"docker-compose -f {compose_file} ps", shell=True)
    
    return success

def verify_setup():
    """Verify the setup is working."""
    print_section("Verification")
    
    # Check if containers are running
    try:
        result = subprocess.run("docker ps --filter name=lightrag --format 'table {{.Names}}\t{{.Status}}'", 
                               shell=True, capture_output=True, text=True)
        print("Container status:")
        print(result.stdout)
    except Exception as e:
        print(f"Error checking containers: {e}")
    
    print("\n🧪 You can now test LightRAG with:")
    print("   python quick_test.py")
    print("   python test_lightrag_docs.py --help")

def main():
    """Main setup function."""
    print_header("LightRAG Storage Setup")
    
    print("This script will help you set up LightRAG with different storage backends.")
    print("You can choose from local file storage to enterprise databases.")
    
    try:
        # Choose storage backend
        config = choose_storage_backend()
        print(f"\n✅ Selected: {config['name']}")
        
        # Setup environment
        if not setup_environment_file(config['config']):
            print("❌ Environment setup failed")
            return False
        
        # Start services
        if not start_services(config['compose'], config['deps']):
            print("❌ Service startup failed")
            return False
        
        # Verify setup
        verify_setup()
        
        print_header("Setup Complete!")
        print("✅ LightRAG is ready to use!")
        
        return True
        
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)