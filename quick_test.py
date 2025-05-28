#!/usr/bin/env python3
"""
Quick test script for LightRAG with sample documentation content.
This can be used to verify the setup before loading large documentation sets.
"""

import os
import asyncio
from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam

# Load environment variables from .env file
load_dotenv()
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

setup_logger("lightrag", level="INFO")

WORKING_DIR = "./rag_storage_test"

# Sample documentation content about Apolo (you can modify this)
SAMPLE_DOCS = [
    """
# Apolo Platform Overview

Apolo is an enterprise-ready platform for AI and machine learning workloads. 
It provides a comprehensive suite of tools for data scientists and ML engineers 
to develop, train, and deploy models at scale.

## Key Features

- **Scalable Computing**: Access to GPU and CPU resources on demand
- **Collaborative Environment**: Shared workspaces and project management
- **Model Deployment**: Easy deployment of trained models to production
- **Data Management**: Secure storage and versioning of datasets
- **Monitoring**: Real-time monitoring of training jobs and deployed models

## Getting Started

To get started with Apolo:
1. Sign up for an account
2. Install the Apolo CLI
3. Create your first project
4. Start training your models
""",
    """
# Apolo Console Applications

Apolo Console provides a web-based interface for managing your ML workloads.
It includes several pre-installed applications and the ability to install custom apps.

## Pre-installed Applications

### Jupyter Lab
Interactive development environment for data science and machine learning.
- Supports Python, R, and Julia kernels
- Git integration
- Collaborative features

### VS Code
Cloud-based development environment with full VS Code functionality.
- Extensions marketplace
- Remote debugging
- Integrated terminal

### MLflow
Experiment tracking and model registry platform.
- Track experiments and metrics
- Compare model performance
- Model versioning and deployment

## Available Custom Apps

### Stable Diffusion
AI image generation using Stable Diffusion models.
- Text-to-image generation
- Image-to-image transformation
- Custom model fine-tuning

### LLM Inference
Deploy and serve large language models.
- Support for popular models (GPT, LLaMA, etc.)
- Auto-scaling inference endpoints
- Multi-GPU support
""",
    """
# Apolo Administration Guide

## User and Quota Management

Administrators can manage users and resource quotas through the Apolo Console.

### Adding Users
1. Navigate to the Users section
2. Click "Add User"
3. Enter user details and assign roles
4. Set resource quotas

### Managing Quotas
Resource quotas control how much compute time and storage each user can consume:
- **CPU Hours**: Maximum CPU time per month
- **GPU Hours**: Maximum GPU time per month  
- **Storage**: Maximum storage allocation
- **Concurrent Jobs**: Number of simultaneous jobs

### Creating Organizations
Organizations help manage teams and projects:
1. Create organization
2. Add members
3. Assign project ownership
4. Set organization-level quotas

## Cluster Management

### Node Pools
Create specialized node pools for different workloads:
- **CPU Pool**: For CPU-intensive tasks
- **GPU Pool**: For ML training and inference
- **Memory Pool**: For memory-intensive workloads

### Monitoring and Reports
- Real-time resource utilization
- Usage reports by user/organization
- Cost tracking and billing
- Performance metrics
"""
]

async def initialize_rag():
    """Initialize the LightRAG instance."""
    if not os.path.exists(WORKING_DIR):
        os.mkdir(WORKING_DIR)
    
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag

async def load_sample_docs(rag):
    """Load sample documentation into LightRAG."""
    print("📚 Loading sample documentation...")
    
    for i, doc in enumerate(SAMPLE_DOCS, 1):
        print(f"  Loading document {i}/{len(SAMPLE_DOCS)}")
        await rag.ainsert(doc)
    
    print(f"✅ Loaded {len(SAMPLE_DOCS)} sample documents")

async def run_sample_queries(rag):
    """Run sample queries to test the system."""
    print("\n🔍 Running sample queries...")
    
    queries = [
        ("What is Apolo and what are its main features?", "hybrid"),
        ("What applications are available in Apolo Console?", "local"),
        ("How do I manage users and quotas?", "global"),
        ("Tell me about LLM inference capabilities", "hybrid")
    ]
    
    for i, (query, mode) in enumerate(queries, 1):
        print(f"\n--- Query {i} ({mode} mode) ---")
        print(f"Q: {query}")
        print("A:", end=" ")
        
        try:
            response = await rag.aquery(query, param=QueryParam(mode=mode))
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 60)

async def main():
    """Main function."""
    print("🚀 LightRAG Quick Test")
    print("=" * 30)
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY environment variable not set!")
        print("Please set it with: export OPENAI_API_KEY=your_api_key")
        return
    
    rag = None
    try:
        # Initialize RAG
        print("🔧 Initializing LightRAG...")
        rag = await initialize_rag()
        
        # Load sample docs
        await load_sample_docs(rag)
        
        # Run sample queries
        await run_sample_queries(rag)
        
        print("\n✅ Quick test completed successfully!")
        print("You can now proceed with the full documentation loading script.")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if rag:
            await rag.finalize_storages()

if __name__ == "__main__":
    asyncio.run(main())