"""
Configuration settings for Apolo Copilot
"""
import os
from typing import Dict, List, Optional
from pydantic import BaseSettings, Field


class LightRAGSettings(BaseSettings):
    """LightRAG connection and configuration"""
    
    # Connection settings
    api_url: str = Field(default="http://localhost:9621", env="LIGHTRAG_API_URL")
    api_key: Optional[str] = Field(default=None, env="LIGHTRAG_API_KEY")
    timeout: int = Field(default=30, env="LIGHTRAG_TIMEOUT")
    
    # Query parameters
    default_mode: str = Field(default="hybrid", env="LIGHTRAG_DEFAULT_MODE")
    max_tokens: int = Field(default=32768, env="LIGHTRAG_MAX_TOKENS")
    
    class Config:
        env_file = ".env"


class LLMSettings(BaseSettings):
    """LLM configuration for evaluation and processing"""
    
    # OpenAI settings  
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    model: str = Field(default="gpt-4o-mini", env="LLM_MODEL")
    temperature: float = Field(default=0.1, env="LLM_TEMPERATURE")
    max_tokens: int = Field(default=4096, env="LLM_MAX_TOKENS")
    
    # Evaluation settings
    evaluation_model: str = Field(default="gpt-4o-mini", env="LLM_EVALUATION_MODEL")
    evaluation_temperature: float = Field(default=0.0, env="LLM_EVALUATION_TEMPERATURE")
    
    class Config:
        env_file = ".env"


class RecursiveRetrievalSettings(BaseSettings):
    """Settings for recursive retrieval and context accumulation"""
    
    # Recursion control
    max_iterations: int = Field(default=5, env="MAX_RECURSION_ITERATIONS")
    max_context_tokens: int = Field(default=16000, env="MAX_CONTEXT_TOKENS")
    
    # Stopping criteria
    completeness_threshold: float = Field(default=0.8, env="COMPLETENESS_THRESHOLD")
    min_new_info_threshold: float = Field(default=0.1, env="MIN_NEW_INFO_THRESHOLD")
    
    # Context management
    summarization_trigger_tokens: int = Field(default=12000, env="SUMMARIZATION_TRIGGER_TOKENS")
    deduplication_similarity_threshold: float = Field(default=0.9, env="DEDUP_SIMILARITY_THRESHOLD")
    
    class Config:
        env_file = ".env"


class ApoloEntitySchema:
    """
    Apolo platform entity and relationship schema for LightRAG
    Based on documentation analysis
    """
    
    # Core platform entities
    ENTITIES = {
        "Job": {
            "description": "Containerized workload/task running on Apolo platform",
            "properties": ["name", "status", "preset", "image", "volumes", "environment", "commands", "cluster"]
        },
        "Image": {
            "description": "Container image used for jobs and applications",
            "properties": ["registry_path", "tags", "build_context", "base_images", "dockerfile"]
        },
        "App": {
            "description": "Pre-installed or available application on the platform",
            "properties": ["name", "type", "category", "dependencies", "configuration", "documentation_url"]
        },
        "Cluster": {
            "description": "Computing infrastructure for running jobs",
            "properties": ["name", "node_pools", "capacity", "location", "status"]
        },
        "Organization": {
            "description": "Collection of users with shared resources and billing",
            "properties": ["name", "users", "projects", "credits", "quotas"]
        },
        "Project": {
            "description": "Collaboration unit containing jobs, images, and artifacts",
            "properties": ["name", "collaborators", "artifacts", "permissions", "organization"]
        },
        "User": {
            "description": "Platform user with roles and resource access",
            "properties": ["username", "roles", "quotas", "organizations", "projects"]
        },
        "Preset": {
            "description": "Resource configuration template for jobs",
            "properties": ["name", "cpu", "memory", "gpu", "disk", "price"]
        },
        "Storage": {
            "description": "File storage and volume management",
            "properties": ["type", "path", "size", "permissions", "mount_point"]
        },
        "CLICommand": {
            "description": "Apolo CLI command with syntax and options",
            "properties": ["command", "syntax", "description", "options", "examples", "category"]
        },
        "Workflow": {
            "description": "Automated process defined in live.yml",
            "properties": ["name", "jobs", "dependencies", "triggers", "outputs"]
        },
        "Secret": {
            "description": "Secure configuration data and credentials",
            "properties": ["name", "type", "scope", "description", "usage"]
        }
    }
    
    # Relationships between entities
    RELATIONSHIPS = {
        "BELONGS_TO": "Entity belongs to another entity (Project belongs to Organization)",
        "CONTAINS": "Entity contains other entities (Organization contains Projects)",
        "USES": "Entity uses another entity (Job uses Image)",
        "RUNS_ON": "Entity runs on infrastructure (Job runs on Cluster)",
        "HAS_ACCESS_TO": "Entity has access permissions (User has access to Project)",
        "MANAGES": "Entity manages another entity (User manages Project)",
        "DEPLOYS": "Entity deploys another entity (App deploys as Job)",
        "BUILDS_FROM": "Entity is built from another (Image builds from Dockerfile)",
        "CONFIGURES": "Entity configures another (Preset configures Job resources)",
        "MOUNTS": "Entity mounts storage (Job mounts Volume)",
        "INHERITS": "Entity inherits from another (User inherits Organization quotas)",
        "REFERENCES": "Entity references another in documentation",
        "DEPENDS_ON": "Entity has dependencies (App depends on Image)",
        "DEFINES": "Entity defines configuration (Workflow defines Jobs)"
    }
    
    # Documentation entity types
    DOCUMENT_ENTITIES = {
        "DocumentationPage": {
            "description": "A page in Apolo documentation",
            "properties": ["title", "url", "section", "subsection", "audience", "content_type"]
        },
        "DocumentChunk": {
            "description": "Chunk of documentation content",
            "properties": ["content", "source_page", "section", "chunk_index", "entity_mentions"]
        },
        "UseCase": {
            "description": "Real-world implementation example or tutorial",
            "properties": ["title", "industry", "technologies", "complexity", "components"]
        },
        "TroubleshootingGuide": {
            "description": "Problem diagnosis and solution documentation",
            "properties": ["problem", "symptoms", "causes", "solutions", "related_issues"]
        }
    }


class Settings:
    """Main configuration class combining all settings"""
    
    def __init__(self):
        self.lightrag = LightRAGSettings()
        self.llm = LLMSettings()
        self.recursive_retrieval = RecursiveRetrievalSettings()
        self.entity_schema = ApoloEntitySchema()
    
    @property
    def all_entities(self) -> Dict:
        """Get combined entity definitions"""
        return {
            **self.entity_schema.ENTITIES,
            **self.entity_schema.DOCUMENT_ENTITIES
        }
    
    @property
    def relationships(self) -> Dict:
        """Get relationship definitions"""
        return self.entity_schema.RELATIONSHIPS


# Global settings instance
settings = Settings()