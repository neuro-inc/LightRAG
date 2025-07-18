# LightRAG Provider Testing Setup

This document provides comprehensive instructions for testing LightRAG with multiple LLM providers using the provider testing stack.

## 🎯 Overview

The LightRAG provider testing setup allows you to run multiple LightRAG instances simultaneously, each configured with different LLM providers. This enables easy comparison and testing of different models and providers.

## 🚀 Quick Start

### 1. Prerequisites
- Docker and Docker Compose installed
- API keys for the providers you want to test
- At least 8GB RAM available for running multiple instances

### 2. Setup Provider Configuration Files

Create and configure the environment files for each provider:

```bash
# Copy the example configurations
cp .env.openai .env.openai.local
cp .env.anthropic .env.anthropic.local
cp .env.gemini .env.gemini.local
cp .env.ollama .env.ollama.local
cp .env.openai-compatible .env.openai-compatible.local

# Edit each file with your API keys
vim .env.openai
vim .env.anthropic
vim .env.gemini
# ... etc
```

### 3. Deploy All Provider Instances

```bash
# Deploy all provider instances
./deploy-stacks.sh deploy providers
```

### 4. Access Provider Instances

Once deployed, you can access each provider instance:

- **OpenAI**: http://localhost:9621/webui
- **Anthropic**: http://localhost:9622/webui  
- **Gemini**: http://localhost:9623/webui
- **Ollama**: http://localhost:9624/webui
- **OpenAI-compatible**: http://localhost:9625/webui

## 📋 Provider Configuration Details

### OpenAI Configuration (`.env.openai`)
```bash
# OpenAI Provider Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
LLM_BINDING=openai
LLM_MODEL=gpt-4o-mini
LLM_BINDING_HOST=https://api.openai.com:443/v1
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=text-embedding-ada-002
EMBEDDING_DIM=1536
```

**Supported Models:**
- `gpt-4o-mini` (recommended for testing)
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`

### Anthropic Configuration (`.env.anthropic`)
```bash
# Anthropic Provider Configuration
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key-here
OPENAI_API_KEY=sk-your-openai-api-key-here  # For embeddings
LLM_BINDING=anthropic
LLM_MODEL=claude-3-opus-20240229
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=text-embedding-ada-002
```

**Supported Models:**
- `claude-3-opus-20240229`
- `claude-3-sonnet-20240229`
- `claude-3-haiku-20240307`

### Gemini Configuration (`.env.gemini`)
```bash
# Gemini Provider Configuration
GEMINI_API_KEY=your-gemini-api-key-here
OPENAI_API_KEY=sk-your-openai-api-key-here  # For embeddings
LLM_BINDING=gemini
LLM_MODEL=gemini-1.5-pro
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=text-embedding-ada-002
```

**Supported Models:**
- `gemini-1.5-pro`
- `gemini-1.5-flash`
- `gemini-pro`

### Ollama Configuration (`.env.ollama`)
```bash
# Ollama Provider Configuration
LLM_BINDING=ollama
LLM_MODEL=llama3.1:8b
LLM_BINDING_HOST=http://lightrag-ollama-server:11434/api
EMBEDDING_BINDING=ollama
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_DIM=1024
```

**Popular Models:**
- `llama3.1:8b`
- `llama3.1:8b-instruct-q4_K_M`
- `mistral:7b`
- `codellama:7b`

**Embedding Models:**
- `nomic-embed-text`
- `mxbai-embed-large`
- `all-minilm`

### OpenAI-Compatible Configuration (`.env.openai-compatible`)
```bash
# OpenAI Compatible Provider Configuration
LLM_BINDING=openai
LLM_MODEL=meta-llama/Llama-3.1-8B-Instruct
LLM_BINDING_HOST=https://my-llm-server.com:8080/
EMBEDDING_BINDING=openai
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_BINDING_HOST=https://my-embedding-server.com:8080/
```

**Compatible with:**
- vLLM deployments
- Text Generation Inference (TGI)
- FastChat
- LocalAI
- Any OpenAI-compatible API

## 🔧 Management Commands

### Starting and Stopping

```bash
# Start all provider instances
./deploy-stacks.sh deploy providers

# Stop all provider instances
./deploy-stacks.sh stop providers

# Clean up all data (removes volumes)
./deploy-stacks.sh cleanup providers
```

### Individual Service Management

```bash
# Check status of all services
docker-compose -f docker-compose.providers.yml ps

# Check logs for specific provider
docker-compose -f docker-compose.providers.yml logs lightrag-openai
docker-compose -f docker-compose.providers.yml logs lightrag-anthropic

# Restart specific service
docker-compose -f docker-compose.providers.yml restart lightrag-ollama
```

## 📊 Testing and Comparison

### Health Checks

Each provider instance has a health endpoint:

```bash
# Check health of all instances
curl http://localhost:9621/health  # OpenAI
curl http://localhost:9622/health  # Anthropic
curl http://localhost:9623/health  # Gemini
curl http://localhost:9624/health  # Ollama
curl http://localhost:9625/health  # OpenAI-compatible
```

### API Usage Examples

```bash
# Upload document to OpenAI instance
curl -X POST "http://localhost:9621/documents" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your document content here"}'

# Query OpenAI instance
curl -X POST "http://localhost:9621/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the main topic?"}'

# Compare with Anthropic instance
curl -X POST "http://localhost:9622/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the main topic?"}'
```

## 🛠 Troubleshooting

### Common Issues

1. **Service won't start**
   ```bash
   # Check logs
   docker-compose -f docker-compose.providers.yml logs lightrag-openai
   
   # Verify API keys are set
   docker-compose -f docker-compose.providers.yml exec lightrag-openai env | grep API_KEY
   ```

2. **Ollama models not available**
   ```bash
   # Pull models manually
   docker-compose -f docker-compose.providers.yml exec ollama ollama pull llama3.1:8b
   docker-compose -f docker-compose.providers.yml exec ollama ollama pull nomic-embed-text
   ```

3. **Port conflicts**
   ```bash
   # Check if ports are already in use
   netstat -tulpn | grep -E ':(9621|9622|9623|9624|9625)'
   ```

### Resource Requirements

- **Minimum**: 8GB RAM, 4 CPU cores
- **Recommended**: 16GB RAM, 8 CPU cores
- **Storage**: 10GB for models and data

### Performance Optimization

```bash
# Reduce resource usage by disabling unused providers
docker-compose -f docker-compose.providers.yml stop lightrag-gemini lightrag-anthropic

# Or deploy only specific providers
docker-compose -f docker-compose.providers.yml up -d postgres lightrag-openai lightrag-ollama
```

## 📚 API Documentation

Each provider instance exposes the same API endpoints:

- **API Docs**: http://localhost:PORT/docs
- **Health**: http://localhost:PORT/health
- **Web UI**: http://localhost:PORT/webui

Replace `PORT` with the specific port for each provider (9621-9625).

## 🔐 Security Considerations

1. **API Keys**: Store API keys securely, never commit them to version control
2. **Network**: Consider using Docker networks for production deployments
3. **Firewall**: Restrict access to ports 9621-9625 in production
4. **Data**: Use volume mounts for persistent data storage

## 📈 Monitoring

```bash
# Monitor resource usage
docker stats

# Monitor specific services
docker-compose -f docker-compose.providers.yml top

# View real-time logs
docker-compose -f docker-compose.providers.yml logs -f lightrag-openai
```

This setup provides a comprehensive testing environment for comparing different LLM providers with LightRAG, making it easy to evaluate performance, accuracy, and cost across different models and providers.