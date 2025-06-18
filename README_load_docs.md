# LightRAG Documentation Loader

Simple script to load markdown documentation into LightRAG.

## Usage

```bash
# Custom documentation path
python load_docs.py /path/to/your/docs

# Custom LightRAG endpoint
python load_docs.py docs/ --endpoint https://lightrag.example.com

# Skip test query after loading
python load_docs.py docs/ --no-test
```

## Features

- **Simple dependency**: Only requires `httpx` and Python standard library
- **Automatic discovery**: Finds all `.md` files recursively
- **Basic metadata**: Adds title, path, and source information
- **Progress tracking**: Shows loading progress with success/failure counts
- **Health checks**: Verifies LightRAG connectivity before loading
- **Test queries**: Validates functionality after loading

## Requirements

```bash
pip install httpx
```

## Use Cases

This loader is perfect for:
- **Kubernetes deployments**: Self-contained with minimal dependencies
- **Quick testing**: Immediate setup without complex environments
- **Documentation loading**: Any markdown-based documentation
- **Development workflows**: Fast iteration and testing

## Requirements

```bash
pip install httpx
```

**Note**: This script is included with LightRAG deployments and provides a simple way to load any markdown documentation into your LightRAG instance.