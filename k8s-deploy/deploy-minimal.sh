#!/bin/bash

# Deploy LightRAG Minimal to Minikube
# This script deploys the minimal LightRAG setup using the standalone lightrag-minimal chart

set -e

NAMESPACE="lightrag"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "🚀 Deploying LightRAG Minimal to Minikube"
echo "================================================"

# Check if OpenAI API key is provided
if [ -z "$OPENAI_API_KEY" ]; then
  echo "❌ OPENAI_API_KEY environment variable is not set"
  echo "Please set your OpenAI API key:"
  echo "export OPENAI_API_KEY='your-api-key-here'"
  echo "Then run this script again."
  exit 1
fi

# Create namespace if it doesn't exist
if ! kubectl get namespace $NAMESPACE &> /dev/null; then
  echo "📦 Creating namespace '$NAMESPACE'..."
  kubectl create namespace $NAMESPACE
else
  echo "✅ Namespace '$NAMESPACE' already exists"
fi

# Add Bitnami repo (for PostgreSQL dependency)
echo "📊 Adding Bitnami Helm repository..."
helm repo add bitnami https://charts.bitnami.com/bitnami 2>/dev/null || true
helm repo update

# Deploy using Helm
echo "🔧 Deploying LightRAG Minimal..."
helm upgrade --install lightrag-minimal "$SCRIPT_DIR/lightrag-minimal" \
  --namespace $NAMESPACE \
  --set secrets.openaiApiKey="$OPENAI_API_KEY" \
  --values "$SCRIPT_DIR/values-minimal.yaml" \
  --wait \
  --timeout=10m

echo ""
echo "⏳ Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=lightrag-minimal --timeout=300s -n $NAMESPACE

echo ""
echo "✅ LightRAG Minimal deployed successfully!"
echo ""
echo "🌐 To access LightRAG, run:"
echo "   kubectl port-forward svc/lightrag-minimal 9621:9621 -n $NAMESPACE"
echo ""
echo "📱 Then open: http://localhost:9621"
echo ""
echo "📊 Monitor the deployment:"
echo "   kubectl get pods -n $NAMESPACE"
echo "   kubectl logs -l app.kubernetes.io/name=lightrag-minimal -n $NAMESPACE -f"
echo ""