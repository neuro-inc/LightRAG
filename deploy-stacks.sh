#!/bin/bash
# Deployment script for LightRAG stack configurations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if .env file exists
check_env_file() {
    local env_file=${1:-.env}
    if [ ! -f "$env_file" ]; then
        print_warning "$env_file file not found. Creating from env.example..."
        if [ -f env.example ]; then
            cp env.example "$env_file"
            print_warning "Please update $env_file with your API keys before deployment!"
        else
            print_error "env.example file not found!"
            exit 1
        fi
    fi
}

# Check provider-specific .env files
check_provider_env_files() {
    local providers=("openai" "anthropic" "gemini" "ollama" "openai-compatible")
    for provider in "${providers[@]}"; do
        local env_file=".env.$provider"
        if [ ! -f "$env_file" ]; then
            print_warning "$env_file file not found. Please create it based on the template."
            print_warning "Example: Copy from .env.openai and modify for $provider"
        fi
    done
}

# Create necessary directories
create_directories() {
    print_status "Creating necessary directories..."
    mkdir -p data/inputs
    mkdir -p data/rag_storage
    mkdir -p data/dev-storage
    print_success "Directories created"
}

# Create provider-specific directories
create_provider_directories() {
    print_status "Creating provider-specific directories..."
    local providers=("openai" "anthropic" "gemini" "ollama" "openai-compatible")
    for provider in "${providers[@]}"; do
        mkdir -p "data/$provider/inputs"
        mkdir -p "data/$provider/rag_storage"
    done
    print_success "Provider directories created"
}

# Deploy specific stack
deploy_stack() {
    local stack=$1
    local compose_file="docker-compose.${stack}.yml"
    
    if [ ! -f "$compose_file" ]; then
        print_error "Compose file $compose_file not found!"
        return 1
    fi
    
    print_status "Deploying $stack stack..."
    
    # Stop any existing containers
    docker-compose -f "$compose_file" down 2>/dev/null || true
    
    # Start the stack
    docker-compose -f "$compose_file" up -d
    
    if [ $? -eq 0 ]; then
        print_success "$stack stack deployed successfully!"
        
        # Show running services
        echo ""
        print_status "Running services:"
        docker-compose -f "$compose_file" ps
        
        # Wait a bit for services to start
        sleep 5
        
        # Check LightRAG health
        print_status "Checking LightRAG health..."
        for i in {1..30}; do
            if curl -s http://localhost:9621/health > /dev/null 2>&1; then
                print_success "LightRAG is healthy and ready!"
                echo ""
                echo "🌐 Web UI: http://localhost:9621/webui"
                echo "📖 API Docs: http://localhost:9621/docs"
                echo "💚 Health Check: http://localhost:9621/health"
                return 0
            fi
            echo -n "."
            sleep 2
        done
        
        print_warning "LightRAG health check timed out. Check logs with:"
        echo "docker-compose -f $compose_file logs lightrag"
    else
        print_error "Failed to deploy $stack stack!"
        return 1
    fi
}

# Deploy providers stack (all providers at once)
deploy_providers_stack() {
    local compose_file="docker-compose.providers.yml"
    
    if [ ! -f "$compose_file" ]; then
        print_error "Compose file $compose_file not found!"
        return 1
    fi
    
    print_status "Deploying providers stack..."
    
    # Stop any existing containers
    docker-compose -f "$compose_file" down 2>/dev/null || true
    
    # Start the stack
    docker-compose -f "$compose_file" up -d
    
    if [ $? -eq 0 ]; then
        print_success "Providers stack deployed successfully!"
        
        # Show running services
        echo ""
        print_status "Running services:"
        docker-compose -f "$compose_file" ps
        
        # Wait a bit for services to start
        sleep 5
        
        # Check health of all PostgreSQL instances first
        print_status "Checking PostgreSQL instances health..."
        local postgres_instances=("postgres-openai:5432" "postgres-anthropic:5433" "postgres-gemini:5434" "postgres-ollama:5435" "postgres-openai-compatible:5436")
        
        for postgres_instance in "${postgres_instances[@]}"; do
            IFS=':' read -r instance port <<< "$postgres_instance"
            echo -n "Checking $instance ($port)... "
            
            for i in {1..10}; do
                if pg_isready -h localhost -p "$port" > /dev/null 2>&1; then
                    echo "✅ Healthy"
                    break
                fi
                if [ $i -eq 10 ]; then
                    echo "❌ Unhealthy (check logs)"
                fi
                sleep 2
            done
        done
        
        echo ""
        
        # Check health of all provider instances
        print_status "Checking provider instances health..."
        echo ""
        
        local providers=("openai:9621" "anthropic:9622" "gemini:9623" "ollama:9624" "openai-compatible:9625")
        
        for provider_port in "${providers[@]}"; do
            IFS=':' read -r provider port <<< "$provider_port"
            echo -n "Checking $provider ($port)... "
            
            for i in {1..15}; do
                if curl -s "http://localhost:$port/health" > /dev/null 2>&1; then
                    echo "✅ Healthy"
                    echo "  🌐 Web UI: http://localhost:$port/webui"
                    echo "  📖 API Docs: http://localhost:$port/docs"
                    break
                fi
                if [ $i -eq 15 ]; then
                    echo "❌ Unhealthy (check logs)"
                fi
                sleep 2
            done
        done
        
        echo ""
        print_success "All provider instances checked!"
        print_status "PostgreSQL instances are available on ports:"
        print_status "  • OpenAI: localhost:5432"
        print_status "  • Anthropic: localhost:5433"
        print_status "  • Gemini: localhost:5434"
        print_status "  • Ollama: localhost:5435"
        print_status "  • OpenAI-compatible: localhost:5436"
        echo ""
        print_status "Use 'docker-compose -f $compose_file logs <service>' to check individual logs"
    else
        print_error "Failed to deploy providers stack!"
        return 1
    fi
}

# Stop stack
stop_stack() {
    local stack=$1
    local compose_file="docker-compose.${stack}.yml"
    
    if [ ! -f "$compose_file" ]; then
        print_error "Compose file $compose_file not found!"
        return 1
    fi
    
    print_status "Stopping $stack stack..."
    docker-compose -f "$compose_file" down
    print_success "$stack stack stopped"
}

# Clean up stack (stop and remove volumes)
cleanup_stack() {
    local stack=$1
    local compose_file="docker-compose.${stack}.yml"
    
    if [ ! -f "$compose_file" ]; then
        print_error "Compose file $compose_file not found!"
        return 1
    fi
    
    print_warning "This will remove all data for $stack stack. Are you sure? (y/N)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        print_status "Cleaning up $stack stack..."
        docker-compose -f "$compose_file" down -v --remove-orphans
        print_success "$stack stack cleaned up"
    else
        print_status "Cleanup cancelled"
    fi
}

# Show usage
show_usage() {
    echo "Usage: $0 <command> [stack]"
    echo ""
    echo "Commands:"
    echo "  deploy <stack>    Deploy a specific stack"
    echo "  stop <stack>      Stop a specific stack"
    echo "  cleanup <stack>   Stop and remove all data for a stack"
    echo "  list              List available stacks"
    echo ""
    echo "Available stacks:"
    echo "  development       File-based storage (NetworkX + NanoVector + JSON)"
    echo "  minimal           File-based storage (NetworkX + PostgreSQL)"
    echo "  balanced          Mixed storage (NetworkX + Qdrant + Redis + PostgreSQL)"
    echo "  high-performance  Specialized storage (Neo4j + Milvus + Redis + PostgreSQL)"
    echo "  all-in-one       Cloud-native (Neo4j + Qdrant + Redis + MongoDB)"
    echo "  providers         All provider instances (OpenAI, Anthropic, Gemini, Ollama, OpenAI-compatible)"
    echo ""
    echo "Examples:"
    echo "  $0 deploy development"
    echo "  $0 stop minimal"
    echo "  $0 cleanup high-performance"
    echo "  $0 deploy providers"
}

# List available stacks
list_stacks() {
    print_status "Available LightRAG stack configurations:"
    echo ""
    echo "📚 development       - File-based storage, perfect for development"
    echo "💰 minimal           - PostgreSQL-based, single database"
    echo "🎯 balanced          - Mixed storage, good performance/complexity balance"
    echo "🏆 high-performance  - Specialized databases, maximum performance"
    echo "🐳 all-in-one       - Cloud-native, containerized services"
    echo "🔧 providers         - All provider testing instances (5 different LLM providers)"
    echo ""
    echo "Provider instances (when deploying 'providers'):"
    echo "  🤖 OpenAI (port 9621)           - OpenAI GPT models"
    echo "  🧠 Anthropic (port 9622)        - Claude models"
    echo "  🔮 Gemini (port 9623)           - Google Gemini models"
    echo "  🦙 Ollama (port 9624)           - Local open-source models"
    echo "  🔌 OpenAI-compatible (port 9625) - Custom OpenAI-compatible APIs"
    echo ""
    echo "Use '$0 deploy <stack>' to deploy a configuration"
}

# Main script logic
main() {
    case "$1" in
        deploy)
            if [ -z "$2" ]; then
                print_error "Please specify a stack to deploy"
                show_usage
                exit 1
            fi
            
            if [ "$2" = "providers" ]; then
                check_provider_env_files
                create_provider_directories
                deploy_providers_stack
            else
                check_env_file
                create_directories
                deploy_stack "$2"
            fi
            ;;
        stop)
            if [ -z "$2" ]; then
                print_error "Please specify a stack to stop"
                show_usage
                exit 1
            fi
            stop_stack "$2"
            ;;
        cleanup)
            if [ -z "$2" ]; then
                print_error "Please specify a stack to cleanup"
                show_usage
                exit 1
            fi
            cleanup_stack "$2"
            ;;
        list)
            list_stacks
            ;;
        *)
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"