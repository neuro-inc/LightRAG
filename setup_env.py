#!/usr/bin/env python3
"""
Environment setup script for LightRAG testing.
This script helps configure the necessary environment variables.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def setup_environment():
    """Setup environment variables for LightRAG."""
    print("🔧 LightRAG Environment Setup")
    print("=" * 40)
    
    # Check if .env file exists
    env_file = ".env"
    if not os.path.exists(env_file):
        print(f"❌ {env_file} not found. Creating from example...")
        if os.path.exists("env.example"):
            import shutil
            shutil.copy("env.example", env_file)
            print(f"✅ Created {env_file} from env.example")
        else:
            print("❌ env.example not found!")
            return False
    
    # Check for OpenAI API key
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("\n⚠️  OpenAI API Key not found in environment!")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY=your_api_key_here")
        print("\nOr add it to your .env file:")
        print("LLM_BINDING_API_KEY=your_api_key_here")
        
        # Ask user if they want to set it now
        response = input("\nDo you want to set it now? (y/n): ").strip().lower()
        if response == 'y':
            api_key = input("Enter your OpenAI API key: ").strip()
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
                # Also update .env file
                with open(env_file, 'a') as f:
                    f.write(f"\nOPENAI_API_KEY={api_key}\n")
                    f.write(f"LLM_BINDING_API_KEY={api_key}\n")
                print("✅ API key set!")
            else:
                print("❌ No API key provided")
                return False
        else:
            print("⏭️  Skipping API key setup")
            return False
    else:
        print("✅ OpenAI API key found")
    
    print("\n📋 Environment Status:")
    print(f"   Working Directory: {os.getcwd()}")
    print(f"   Environment File: {'✅' if os.path.exists(env_file) else '❌'}")
    print(f"   OpenAI API Key: {'✅' if os.getenv('OPENAI_API_KEY') else '❌'}")
    
    return True

def check_dependencies():
    """Check if required Python packages are installed."""
    print("\n📦 Checking Dependencies...")
    
    required_packages = [
        "lightrag",
        "openai", 
        "tiktoken",
        "asyncio"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ All dependencies are installed!")
    return True

def main():
    """Main setup function."""
    print("Starting LightRAG environment setup...\n")
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Setup environment
    env_ok = setup_environment()
    
    print("\n" + "=" * 50)
    if deps_ok and env_ok:
        print("✅ Setup complete! You can now run the test script:")
        print("   python test_lightrag_docs.py --help")
        print("   python test_lightrag_docs.py --docs-path /path/to/your/apolo-documentation")
    else:
        print("❌ Setup incomplete. Please address the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()