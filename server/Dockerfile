ARG LIGHTRAG_IMAGE=ghcr.io/hkuds/lightrag:v1.5.7@sha256:5bdbd524931b011df246fe20888d110cef691e6804c12cde636a2b746d7de27e
FROM ${LIGHTRAG_IMAGE}

LABEL org.opencontainers.image.source="https://github.com/neuro-inc/LightRAG"

RUN uv pip install --python /app/.venv/bin/python --no-cache "sentry-sdk==2.71.0"

COPY patches /tmp/patches
RUN apt-get update \
    && apt-get install -y --no-install-recommends patch \
    && for target in /app "$(/app/.venv/bin/python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"; do \
        for p in /tmp/patches/*.patch; do patch -p1 --forward --fuzz=0 --no-backup-if-mismatch -d "$target" < "$p" || exit 1; done; \
    done \
    && apt-get purge -y --auto-remove patch \
    && rm -rf /var/lib/apt/lists/* /tmp/patches

COPY --chown=lightrag:lightrag lightrag_sentry.py /app/lightrag_sentry.py
COPY check_base.py /tmp/check_base.py
RUN PYTHONPATH=/app python /tmp/check_base.py && rm /tmp/check_base.py

CMD ["python", "-m", "lightrag_sentry"]
