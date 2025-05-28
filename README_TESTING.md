# LightRAG Documentation Testing Setup

This directory contains scripts to test LightRAG with your Apolo documentation repository.

## What LightRAG Uses Under the Hood

LightRAG supports multiple storage backends:

**Vector Databases (for embeddings):**
- NanoVectorDB (default, local)
- Milvus, Qdrant, ChromaDB
- PostgreSQL with pgvector
- FAISS (Facebook AI Similarity Search)

**Graph Databases (for knowledge graphs):**
- NetworkX (default, in-memory)
- Neo4j, PostgreSQL, Apache AGE
- MongoDB, Gremlin-compatible DBs

**Key-Value Storage (for metadata/cache):**
- JSON files (default, local)
- Redis, PostgreSQL, MongoDB

## Files Created

### Main Scripts
- **`test_lightrag_docs.py`** - Main script to load documentation and run queries
- **`quick_test.py`** - Quick test with sample content to verify setup
- **`setup_storage.py`** - 🆕 Complete storage backend setup wizard

### Configuration Files  
- **`docker-compose.full.yml`** - Full stack with all databases
- **`.env.default`** - Local storage configuration (no external DBs)
- **`.env.postgres`** - PostgreSQL + pgvector configuration
- **`.env.neo4j`** - Neo4j + Qdrant + Redis configuration

### Database Initialization
- **`init-scripts/`** - PostgreSQL initialization scripts
- **`mongo-init/`** - MongoDB initialization scripts

## Prerequisites

1. **OpenAI API Key** - Required for embeddings and LLM calls
2. **Docker & Docker Compose** - For database services
3. **Python Dependencies** - LightRAG and its dependencies
4. **Documentation Path** - Path to your `apolo-documentation` directory

## 🚀 Quick Start Guide

### Step 1: Choose Your Storage Backend

Run the interactive setup wizard:

```bash
python setup_storage.py
```

This will guide you through:
1. **Storage Backend Selection** (Local, PostgreSQL, Neo4j+Qdrant, or Full Stack)
2. **Environment Configuration** (OpenAI API key setup)
3. **Docker Services** (Start required databases)
4. **Verification** (Check everything is working)

**Available Options:**
- **Local Storage** - No external databases (fastest setup)
- **PostgreSQL** - Enterprise-grade with pgvector for embeddings
- **Neo4j + Qdrant** - Specialized graph + vector databases
- **Full Stack** - All databases for testing different backends

### Step 2: Quick Verification

Test the setup with sample content:

```bash
# This should work after setup_storage.py
python quick_test.py
```

### Step 3: Load Your Documentation

Load your actual Apolo documentation:

```bash
# Basic usage (loads all markdown files)
python test_lightrag_docs.py --docs-path /path/to/your/apolo-documentation

# Test with limited files first (recommended)
python test_lightrag_docs.py --docs-path /path/to/your/apolo-documentation --max-files 10 --test-queries

# Just run test queries on existing data
python test_lightrag_docs.py --skip-loading --test-queries

# Interactive mode only
python test_lightrag_docs.py --skip-loading --interactive
```

## 📋 Step-by-Step Example

Here's exactly how to run everything:

```bash
# 1. Clone/navigate to LightRAG directory
cd /Users/taddeusbuica/Desktop/experiments/LightRAG

# 2. Set up storage (interactive wizard)
python setup_storage.py

# 3. Test with sample content
python quick_test.py

# 4. Load 5 documentation files and test
python test_lightrag_docs.py --docs-path ~/apolo-documentation --max-files 5 --test-queries

# 5. Interactive queries
python test_lightrag_docs.py --skip-loading --interactive

# 6. Load full documentation (when ready)
python test_lightrag_docs.py --docs-path ~/apolo-documentation
```

## Script Options

### test_lightrag_docs.py

```bash
python test_lightrag_docs.py --help

Options:
  --docs-path PATH      Path to documentation directory (default: ../apolo-documentation)
  --max-files N         Maximum number of files to process (for testing)
  --skip-loading        Skip loading docs (use existing data)
  --test-queries        Run predefined test queries
  --interactive         Run in interactive mode
```

**Examples:**

```bash
# Load first 5 files and run test queries
python test_lightrag_docs.py --docs-path ~/apolo-documentation --max-files 5 --test-queries

# Interactive mode with existing data
python test_lightrag_docs.py --skip-loading --interactive

# Full load and both test + interactive modes
python test_lightrag_docs.py --docs-path ~/apolo-documentation
```

## Test Queries

The script includes predefined test queries:

1. **"What is Apolo and what are its main features?"** (hybrid mode)
2. **"How do I install and get started with Apolo?"** (hybrid mode)
3. **"What apps are available in Apolo Console?"** (local mode)
4. **"How do I manage users and quotas in Apolo?"** (global mode)
5. **"What are the machine learning capabilities of Apolo?"** (hybrid mode)
6. **"How to deploy models using LLM inference on Apolo?"** (local mode)

## Interactive Mode

In interactive mode, you can:
- Ask custom questions about the documentation
- Specify search modes (hybrid, local, global)
- Get real-time responses

**Mode specification:**
```
❓ Your question: mode:local What Jupyter features are available?
❓ Your question: mode:global Tell me about Apolo's architecture
❓ Your question: What is MLflow?  # Uses hybrid mode (default)
```

## Query Modes

- **hybrid** - Combines local and global search (recommended for most queries)
- **local** - Searches within document chunks (good for specific details)
- **global** - Searches relationships and entities (good for conceptual questions)

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   ```
   ❌ OPENAI_API_KEY environment variable not set!
   ```
   **Solution:** Set your API key: `export OPENAI_API_KEY=your_key`

2. **Documentation Path Not Found**
   ```
   ❌ Documentation path does not exist: ../apolo-documentation
   ```
   **Solution:** Provide correct path: `--docs-path /correct/path/to/docs`

3. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'lightrag'
   ```
   **Solution:** Install dependencies: `pip install lightrag openai tiktoken`

4. **Docker Container Issues**
   ```bash
   # Check container status
   docker-compose ps
   
   # View logs
   docker-compose logs lightrag
   
   # Restart container
   docker-compose restart lightrag
   ```

### Performance Tips

1. **Start Small** - Use `--max-files` to test with a subset first
2. **Use Existing Data** - Use `--skip-loading` to avoid reprocessing
3. **Monitor Resources** - Large document sets require significant processing time

## File Structure

After running the scripts, you'll have:

```
LightRAG/
├── rag_storage/           # Main RAG storage (full docs)
├── rag_storage_test/      # Test storage (quick test)
├── data/                  # Docker volumes
├── test_lightrag_docs.py  # Main testing script
├── quick_test.py          # Quick verification script
├── setup_env.py           # Environment setup
└── README_TESTING.md      # This file
```

## Next Steps

1. Run `quick_test.py` to verify your setup
2. Load a small subset of docs with `--max-files 10`
3. Test with predefined queries
4. Try interactive mode for custom questions
5. Load the full documentation set
6. Experiment with different query modes

Happy testing! 🚀