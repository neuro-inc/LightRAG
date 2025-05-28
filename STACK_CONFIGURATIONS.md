# LightRAG Stack Configurations

This directory contains Docker Compose configurations for 5 different LightRAG deployment scenarios, each optimized for different use cases and requirements.

## 🚀 Quick Start

### 1. Choose Your Stack

| Stack | Use Case | Resources | Complexity |
|-------|----------|-----------|------------|
| 📚 [Development](#-development-stack) | Local dev, testing | Low | Simple |
| 💰 [Cost-Effective](#-cost-effective-stack) | Budget production | Medium | Simple |
| 🎯 [Balanced](#-balanced-stack) | Standard production | Medium | Medium |
| 🏆 [High-Performance](#-high-performance-stack) | Enterprise, high-scale | High | Complex |
| 🐳 [All-in-One](#-all-in-one-stack) | Cloud-native | Medium | Medium |

### 2. Deploy

```bash
# Using the deployment script (recommended)
./deploy-stacks.sh deploy <stack-name>

# Or manually with docker-compose
docker-compose -f docker-compose.<stack-name>.yml up -d
```

### 3. Access

- **Web UI**: http://localhost:9621/webui
- **API Docs**: http://localhost:9621/docs
- **Health Check**: http://localhost:9621/health

## 📋 Prerequisites

1. **Docker & Docker Compose** installed
2. **Environment file** configured:
   ```bash
   cp env.example .env
   # Edit .env with your OpenAI API key
   ```
3. **Sufficient resources** for your chosen stack

## 📚 Development Stack

**File**: `docker-compose.development.yml`

**Best for**: Local development, testing, learning LightRAG

**Storage Configuration**:
- Graph: NetworkX (file-based)
- Vector: NanoVectorDB (file-based)  
- KV: JSON (file-based)
- Doc Status: JSON (file-based)

**Services**: LightRAG only

**Resources**:
- CPU: 2 cores
- Memory: 4GB
- Storage: 10GB

**Deploy**:
```bash
./deploy-stacks.sh deploy development
```

**Pros**:
- ✅ Zero infrastructure setup
- ✅ Fast startup
- ✅ Portable and lightweight
- ✅ Perfect for development

**Cons**:
- ❌ Limited scalability
- ❌ No concurrent access
- ❌ Single point of failure

## 💰 Cost-Effective Stack

**File**: `docker-compose.cost-effective.yml`

**Best for**: Budget-conscious production, small to medium deployments

**Storage Configuration**:
- Graph: NetworkX (file-based)
- Vector: PostgreSQL + pgvector
- KV: PostgreSQL
- Doc Status: PostgreSQL

**Services**: LightRAG + PostgreSQL

**Resources**:
- CPU: 4 cores
- Memory: 8GB
- Storage: 50GB

**Deploy**:
```bash
./deploy-stacks.sh deploy cost-effective
```

**Pros**:
- ✅ Single database to manage
- ✅ ACID compliance
- ✅ Good performance for medium scale
- ✅ Cost-effective

**Cons**:
- ❌ Graph operations not optimized
- ❌ Vector search not specialized
- ❌ Single database bottleneck

## 🎯 Balanced Stack

**File**: `docker-compose.balanced.yml`

**Best for**: Standard production deployments prioritizing simplicity

**Storage Configuration**:
- Graph: NetworkX (file-based)
- Vector: Qdrant
- KV: Redis
- Doc Status: PostgreSQL

**Services**: LightRAG + Qdrant + Redis + PostgreSQL

**Resources**:
- CPU: 8 cores
- Memory: 16GB
- Storage: 100GB

**Deploy**:
```bash
./deploy-stacks.sh deploy balanced
```

**Pros**:
- ✅ Specialized vector search (Qdrant)
- ✅ Fast KV operations (Redis)
- ✅ Good balance of performance/complexity
- ✅ Easier than high-performance stack

**Cons**:
- ❌ Graph operations still file-based
- ❌ Multiple services to manage
- ❌ Higher resource usage

## 🏆 High-Performance Stack

**File**: `docker-compose.high-performance.yml`

**Best for**: Enterprise deployments, complex graph analytics, high-scale

**Storage Configuration**:
- Graph: Neo4j
- Vector: Milvus
- KV: Redis
- Doc Status: PostgreSQL

**Services**: LightRAG + Neo4j + Milvus + etcd + MinIO + Redis + PostgreSQL

**Resources**:
- CPU: 16+ cores
- Memory: 32GB+
- Storage: 500GB+

**Deploy**:
```bash
./deploy-stacks.sh deploy high-performance
```

**Pros**:
- ✅ Maximum performance for all storage types
- ✅ Advanced graph analytics (Neo4j)
- ✅ Billion-scale vector search (Milvus)
- ✅ Production-ready scalability

**Cons**:
- ❌ High complexity
- ❌ Resource intensive
- ❌ Multiple services to monitor
- ❌ Higher costs

## 🐳 All-in-One Stack

**File**: `docker-compose.all-in-one.yml`

**Best for**: Cloud-native deployments, containerized environments

**Storage Configuration**:
- Graph: Neo4j
- Vector: Qdrant
- KV: Redis
- Doc Status: MongoDB

**Services**: LightRAG + Neo4j + Qdrant + Redis + MongoDB

**Resources**:
- CPU: 8 cores
- Memory: 16GB
- Storage: 100GB

**Deploy**:
```bash
./deploy-stacks.sh deploy all-in-one
```

**Pros**:
- ✅ Cloud-native services
- ✅ Good performance across all storage types
- ✅ Container-optimized
- ✅ Kubernetes-ready

**Cons**:
- ❌ More services than balanced stack
- ❌ Higher operational overhead
- ❌ Complex monitoring setup

## 🛠️ Deployment Script Usage

The `deploy-stacks.sh` script provides easy management of all configurations:

### Deploy a Stack
```bash
./deploy-stacks.sh deploy <stack-name>
```

### Stop a Stack
```bash
./deploy-stacks.sh stop <stack-name>
```

### Clean Up (Remove All Data)
```bash
./deploy-stacks.sh cleanup <stack-name>
```

### List Available Stacks
```bash
./deploy-stacks.sh list
```

## 🔧 Customization

### Environment Variables

Key environment variables in `.env`:

```bash
# LLM Configuration
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4o-mini
MAX_ASYNC=4
MAX_TOKENS=32768

# Performance Tuning
ENABLE_LLM_CACHE=true
ENABLE_LLM_CACHE_FOR_EXTRACT=true
TIMEOUT=240

# Storage-specific settings
POSTGRES_MAX_CONNECTIONS=20
NEO4J_MEMORY_HEAP_MAX_SIZE=2G
REDIS_MAXMEMORY=1gb
```

### Resource Adjustment

To adjust resources for any stack, modify the service definitions:

```yaml
# Example: Increase PostgreSQL memory
postgres:
  environment:
    POSTGRES_SHARED_BUFFERS: 1GB
    POSTGRES_EFFECTIVE_CACHE_SIZE: 2GB
```

### Port Configuration

Default ports for each service:

| Service | Port | Stack |
|---------|------|-------|
| LightRAG | 9621 | All |
| PostgreSQL | 5432 | Cost-Effective, Balanced, High-Performance |
| Redis | 6379 | Balanced, High-Performance, All-in-One |
| Neo4j HTTP | 7474 | High-Performance, All-in-One |
| Neo4j Bolt | 7687 | High-Performance, All-in-One |
| Qdrant | 6333 | Balanced, All-in-One |
| Milvus | 19530 | High-Performance |
| MongoDB | 27017 | All-in-One |

## 🔍 Monitoring & Troubleshooting

### Health Checks

All configurations include health checks. Check service status:

```bash
# View all services
docker-compose -f docker-compose.<stack>.yml ps

# Check specific service logs
docker-compose -f docker-compose.<stack>.yml logs <service-name>

# Follow logs in real-time
docker-compose -f docker-compose.<stack>.yml logs -f lightrag
```

### Common Issues

1. **Port Conflicts**: Change port mappings if conflicts occur
2. **Memory Issues**: Reduce heap sizes for Neo4j/JVM services
3. **API Key Errors**: Ensure `.env` file has valid OpenAI API key
4. **Permission Issues**: Check Docker volume permissions

### Performance Monitoring

For production deployments, consider adding:

- **Prometheus** + **Grafana** for metrics
- **ELK Stack** for log aggregation
- **Jaeger** for distributed tracing

## 🔄 Migration Between Stacks

### Development → Cost-Effective
1. Export data: `./deploy-stacks.sh stop development`
2. Copy `./data/rag_storage` to backup
3. Deploy new stack: `./deploy-stacks.sh deploy cost-effective`
4. Import data through LightRAG API

### Cost-Effective → Balanced
1. Stop current stack
2. Backup PostgreSQL data
3. Deploy balanced stack
4. Migrate PostgreSQL data, reimport vectors to Qdrant

### Balanced → High-Performance
1. Export graph data from NetworkX files
2. Export vectors from Qdrant
3. Deploy high-performance stack  
4. Import to Neo4j and Milvus

## 📊 Performance Comparison

| Metric | Development | Cost-Effective | Balanced | High-Performance | All-in-One |
|--------|-------------|----------------|----------|------------------|------------|
| **Startup Time** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Vector Search** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Graph Queries** | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Scalability** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Complexity** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Cost** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 🎯 Recommendations

### Choose Development Stack If:
- Learning LightRAG
- Local development
- Quick prototyping
- Limited resources

### Choose Cost-Effective Stack If:
- Small to medium production deployment
- Budget constraints
- Simple operational requirements
- <100K documents

### Choose Balanced Stack If:
- Standard production deployment
- Need good vector search performance
- Moderate operational complexity acceptable
- 100K-1M documents

### Choose High-Performance Stack If:
- Enterprise deployment
- Complex graph analytics required
- High concurrent users
- >1M documents
- Performance is critical

### Choose All-in-One Stack If:
- Cloud-native deployment
- Kubernetes environment
- Need multiple specialized databases
- Container orchestration preferred

---

*For detailed analysis of trade-offs and performance characteristics, see [REPORT.md](REPORT.md)*