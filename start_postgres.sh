#!/bin/bash
# Start LightRAG with PostgreSQL only

# Load environment variables from .env file
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

echo "🚀 Starting LightRAG with PostgreSQL"
echo "===================================="

# Check if .env exists, otherwise copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from env.example..."
    cp env.example .env
    echo "⚠️  Please update .env with your actual API keys!"
else
    echo "📋 Using existing .env configuration..."
fi

# Clean up and start
echo "🧹 Cleaning up..."
docker-compose -f docker-compose.full.yml down

echo "📊 Starting PostgreSQL..."
docker-compose -f docker-compose.full.yml up -d postgres

echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 10

echo "💡 Starting LightRAG..."
docker-compose -f docker-compose.full.yml up -d lightrag

echo "✅ PostgreSQL setup complete!"
echo ""
echo "Services:"
echo "- LightRAG: http://localhost:9621"
echo "- PostgreSQL: localhost:5432"
echo ""
echo "Test with: python quick_test.py"