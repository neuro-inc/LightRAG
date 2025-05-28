# Apolo Copilot

An intelligent assistant powered by LightRAG that provides comprehensive help with the Apolo platform through recursive retrieval and context-aware responses.

## Overview

Apolo Copilot leverages LightRAG's graph-powered retrieval system with recursive querying and stateful context accumulation to provide intelligent assistance for:

- **Platform Navigation**: Help users understand Apolo's features and capabilities
- **CLI Assistance**: Detailed command help and usage examples  
- **Troubleshooting**: Context-aware problem diagnosis and solutions
- **Best Practices**: Recommendations based on documentation and use cases
- **Multi-hop Queries**: Complex questions requiring information from multiple sources

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│   LangGraph      │───▶│  Final Answer   │
└─────────────────┘    │   Orchestrator   │    └─────────────────┘
                       └──────────────────┘
                               │
                       ┌──────────────────┐
                       │ Recursive RAG    │
                       │                  │
                       │ ┌──────────────┐ │
                       │ │  LightRAG    │ │
                       │ │  Retrieval   │ │
                       │ └──────────────┘ │
                       │ ┌──────────────┐ │
                       │ │ LLM Context  │ │
                       │ │  Evaluator   │ │
                       │ └──────────────┘ │
                       │ ┌──────────────┐ │
                       │ │   Context    │ │
                       │ │   Reducer    │ │
                       │ └──────────────┘ │
                       └──────────────────┘
```

## Features

### 🔄 Recursive Retrieval
- Iteratively refines queries based on LLM evaluation
- Explores graph connections to gather comprehensive context
- Stops when sufficient information is gathered

### 🧠 Context Accumulation
- Maintains state across retrieval iterations
- Deduplicates and summarizes information
- Preserves important details and source references

### 📊 Knowledge Graph
- Rich entity and relationship modeling for Apolo platform
- Hierarchical documentation structure
- Cross-reference capabilities between CLI, Console, and concepts

### 🎯 Intelligent Query Processing
- Query refinement based on context gaps
- Multi-modal retrieval (local, global, hybrid)
- Source citation and provenance tracking

## Quick Start

1. **Prerequisites**: Ensure LightRAG is running (docker-compose.minimal.yml)
2. **Install dependencies**: `pip install -r requirements.txt`  
3. **Load documentation**: `python -m src.data.loader`
4. **Start assistant**: `python -m src.main`

## Project Structure

```
apolo-copilot/
├── src/
│   ├── agents/          # LangGraph agents and workflow nodes
│   ├── data/           # Documentation loading and preprocessing  
│   ├── retrieval/      # LightRAG integration and recursive logic
│   ├── reducers/       # Context accumulation and summarization
│   └── utils/          # Helper functions and utilities
├── config/             # Configuration files and schemas
├── tests/              # Unit and integration tests
├── docs/               # Project documentation
└── requirements.txt    # Python dependencies
```

## Configuration

Key configuration in `config/settings.py`:

- **LightRAG Connection**: API endpoint and authentication
- **LLM Settings**: Model selection and parameters  
- **Retrieval Parameters**: Recursion depth, stopping criteria
- **Entity Schema**: Apolo platform knowledge graph structure

## Development Status

This project is in active development following the implementation plan in `../blueprints/PLAN.md`. See `../blueprints/PlanProgress.md` for current status.

## Contributing

This project follows the phased implementation approach:
1. **Phase 0**: Foundation & Setup ⏳
2. **Phase 1**: Core LightRAG Implementation 
3. **Phase 2**: Recursive Retrieval & Reducer Logic
4. **Phase 3**: LangGraph Integration
5. **Phase 4**: Evaluation & Optimization
6. **Phase 5**: Deployment & Maintenance

See the blueprint documents for detailed implementation guidelines.