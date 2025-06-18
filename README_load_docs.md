# LightRAG Documentation Loader

Simple script to load markdown documentation into LightRAG.

## Usage

```bash
# Basic usage with default Apolo documentation
python load_docs.py ../apolo-copilot/docs/official-apolo-documentation/docs

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

## Comparison with Advanced Loader

| Feature | This Script | apolo-copilot/load_docs.py |
|---------|-------------|---------------------------|
| Dependencies | httpx only | Full project environment |
| Processing | Basic markdown loading | Advanced entity extraction |
| Setup time | Immediate | Requires poetry install |
| Use case | Quick testing/deployment | Production knowledge base |

For production deployments with rich metadata and entity extraction, use the advanced loader in the `apolo-copilot` directory.