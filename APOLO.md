# APOLO Deployment Notes

This document captures the workflow for building and publishing the Helm charts that power Apolo Copilot and the broader platform deployments.

## Package the Helm Chart

Use Helm’s `package` command to build the chart tarball. Run the command from the repository root so the relative paths resolve correctly.

```bash
helm package k8s-deploy/lightrag-minimal \
  --version v25.10.5 \
  --app-version v25.10.5 \
  -d dist/charts
```

- `k8s-deploy/lightrag-minimal`: chart directory tailored for Apolo Copilot.
- `--version` / `--app-version`: keep these in sync with the release tag you intend to ship.
- `-d dist/charts`: outputs `lightrag-minimal-v25.10.5.tgz` under `dist/charts/`.

## Push the Chart to GHCR

Once the package exists, push it to our OCI-backed Helm registry:

```bash
helm push dist/charts/lightrag-minimal-v25.10.5.tgz oci://ghcr.io/neuro-inc/helm-charts
```

Make sure you are authenticated to `ghcr.io` (via `helm registry login` or Docker login) before pushing.

## Chart Variants

We maintain two Helm charts under `k8s-deploy/`:

1. `k8s-deploy/lightrag-minimal`: the Apolo Copilot deployment bundle. It ships `pgvector` alongside LightRAG so Copilot teams can spin up the full stack quickly.
2. `k8s-deploy/lightrag`: the platform-facing chart that deploys just LightRAG. Platform apps use this chart when installing LightRAG through the Apolo Console or other cluster automation.

## Local Testing

To run the minimal stack locally (matching what the Copilot chart installs), use the provided compose file:

```bash
docker compose -f docker-compose.minimal.yml up
```

This brings up LightRAG plus the pgvector dependency so you can validate changes before cutting a Helm release.
