#!/bin/bash
# Start LightRAG with full database stack

# Load environment variables from .env file
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

echo "🚀 Starting LightRAG Full Stack"
echo "================================"

# Clean up any existing containers
echo "🧹 Cleaning up existing containers..."
docker-compose -f docker-compose.full.yml down

# Start PostgreSQL first
echo "📊 Starting PostgreSQL..."
docker-compose -f docker-compose.full.yml up -d postgres

# Wait a bit
sleep 5

# Start Redis and Qdrant
echo "🔴 Starting Redis and Qdrant..."
docker-compose -f docker-compose.full.yml up -d redis qdrant

# Wait a bit
sleep 5

# Start Neo4j
echo "🕸️  Starting Neo4j..."
docker-compose -f docker-compose.full.yml up -d neo4j

# Wait a bit
sleep 10

# Start LightRAG
echo "💡 Starting LightRAG..."
docker-compose -f docker-compose.full.yml up -d lightrag

echo "✅ Full stack started!"
echo ""
echo "Services:"
echo "- LightRAG: http://localhost:9621"
echo "- PostgreSQL: localhost:5432"
echo "- Redis: localhost:6380"
echo "- Neo4j: http://localhost:7475"
echo "- Qdrant: http://localhost:6333"
echo ""
echo "Check status with: docker-compose -f docker-compose.full.yml ps"