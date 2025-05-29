# LightRAG Minimal Helm Chart

This Helm chart deploys a minimal LightRAG setup that matches the `docker-compose.minimal.yml` configuration for Kubernetes environments.

## Configuration

This chart provides a minimal LightRAG deployment with:
- **PostgreSQL**: For vector storage, KV storage, and document status
- **NetworkX**: For graph storage (local, no external database required)
- **Persistent Storage**: For data persistence across pod restarts
- **Health Checks**: Automated health monitoring

## Prerequisites

- Kubernetes 1.19+
- Helm 3.0+
- OpenAI API key
- Storage class that supports ReadWriteOnce (if using persistent storage)

## Installation

1. **Add the required repository** (if using PostgreSQL subchart):
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

2. **Create a values file** with your configuration:
```yaml
# values-prod.yaml
secrets:
  openaiApiKey: "your-openai-api-key-here"

postgresql:
  auth:
    password: "secure-database-password"

resources:
  limits:
    cpu: 2000m
    memory: 4Gi
  requests:
    cpu: 500m
    memory: 1Gi

persistence:
  ragStorage:
    size: 50Gi
  inputs:
    size: 20Gi
```

3. **Install the chart**:
```bash
helm install lightrag-minimal ./lightrag-minimal -f values-prod.yaml
```

## Configuration Options

### Core Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of LightRAG replicas | `1` |
| `image.repository` | LightRAG image repository | `ghcr.io/hkuds/lightrag` |
| `image.tag` | LightRAG image tag | `latest` |

### Storage Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `persistence.enabled` | Enable persistent storage | `true` |
| `persistence.ragStorage.size` | RAG storage volume size | `20Gi` |
| `persistence.inputs.size` | Inputs storage volume size | `10Gi` |

### PostgreSQL Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `postgresql.enabled` | Deploy PostgreSQL as part of this chart | `true` |
| `postgresql.auth.database` | PostgreSQL database name | `lightrag` |
| `postgresql.auth.username` | PostgreSQL username | `lightrag_user` |
| `postgresql.auth.password` | PostgreSQL password | `lightrag_pass` |

### LightRAG Environment

| Parameter | Description | Default |
|-----------|-------------|---------|
| `env.LLM_MODEL` | OpenAI model to use | `gpt-4o-mini` |
| `env.EMBEDDING_MODEL` | Embedding model | `text-embedding-ada-002` |
| `env.LIGHTRAG_GRAPH_STORAGE` | Graph storage type | `NetworkXStorage` |

## Accessing LightRAG

### Local Development (Port Forward)
```bash
kubectl port-forward svc/lightrag-minimal 9621:9621
```
Then access: http://localhost:9621

### Production (Ingress)
Enable ingress in your values file:
```yaml
ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: lightrag.yourdomain.com
      paths:
        - path: /
          pathType: Prefix
```

## Monitoring

### Check Deployment Status
```bash
kubectl get pods -l app.kubernetes.io/name=lightrag-minimal
kubectl get services -l app.kubernetes.io/name=lightrag-minimal
```

### View Logs
```bash
kubectl logs -l app.kubernetes.io/name=lightrag-minimal -f
```

### Health Checks
The deployment includes health checks on `/health` endpoint.

## Scaling

For production workloads, consider enabling autoscaling:
```yaml
autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

## Upgrading

```bash
helm upgrade lightrag-minimal ./lightrag-minimal -f values-prod.yaml
```

## Uninstalling

```bash
helm uninstall lightrag-minimal
```

**Note**: This will delete all data unless you have persistent volumes with a retain policy.

## Troubleshooting

### Common Issues

1. **Pod not starting**: Check if OpenAI API key is set correctly
2. **Database connection errors**: Verify PostgreSQL is running and accessible
3. **Storage issues**: Ensure your cluster has a default storage class

### Debug Commands
```bash
# Check pod status
kubectl describe pod -l app.kubernetes.io/name=lightrag-minimal

# Check logs
kubectl logs -l app.kubernetes.io/name=lightrag-minimal --previous

# Check secrets
kubectl get secrets lightrag-minimal-secrets -o yaml
```

## Comparison with Docker Compose

This Helm chart provides the same functionality as `docker-compose.minimal.yml`:

| Feature | Docker Compose | Helm Chart |
|---------|----------------|------------|
| PostgreSQL | External container | Embedded subchart |
| NetworkX Storage | Local volume | Persistent volume |
| API Access | Port 9621 | Service + optional Ingress |
| Configuration | .env file | ConfigMap + Secrets |
| Scaling | Manual | Kubernetes native |

## Development

For local development and testing of this chart:

```bash
# Lint the chart
helm lint ./lightrag-minimal

# Template and review
helm template lightrag-minimal ./lightrag-minimal

# Install with debug
helm install lightrag-minimal ./lightrag-minimal --debug --dry-run
```