"""
Documentation loader for Apolo platform documentation.
Processes markdown files and prepares them for LightRAG indexing.
"""

import os
import re
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class DocumentMetadata:
    """Metadata for a documentation file"""
    file_path: str
    relative_path: str
    title: str
    section: str
    subsection: Optional[str]
    audience: str  # admin, user, developer
    content_type: str  # guide, reference, tutorial, troubleshooting
    last_modified: Optional[str] = None


@dataclass
class ProcessedDocument:
    """A processed documentation document"""
    content: str
    metadata: DocumentMetadata
    entities_mentioned: List[str]
    cli_commands: List[str]


class DocumentationLoader:
    """
    Loads and processes Apolo documentation files for LightRAG indexing.
    
    Handles the hierarchical structure of documentation and extracts
    relevant metadata for entity and relationship identification.
    """
    
    def __init__(self, docs_root: str = "../apolo-documentation"):
        self.docs_root = Path(docs_root).resolve()
        self.processed_docs: List[ProcessedDocument] = []
        
        # Documentation structure mapping
        self.section_mapping = {
            "docs/administration": {"audience": "admin", "content_type": "guide"},
            "docs/apolo-concepts-cli": {"audience": "user", "content_type": "reference"},
            "docs/apolo-console": {"audience": "user", "content_type": "guide"},
            "docs/getting-started": {"audience": "user", "content_type": "tutorial"},
            "use-cases": {"audience": "developer", "content_type": "tutorial"},
            "apolo-actions": {"audience": "developer", "content_type": "reference"},
            "apolo-python-sdk": {"audience": "developer", "content_type": "reference"}
        }
        
        # Common Apolo entities to look for in content
        self.apolo_entities = [
            "job", "jobs", "image", "images", "app", "apps", "cluster", "clusters",
            "organization", "organizations", "project", "projects", "user", "users",
            "preset", "presets", "storage", "volume", "volumes", "secret", "secrets",
            "workflow", "workflows", "nodepool", "node-pool", "node-pools"
        ]
        
        # CLI command patterns
        self.cli_patterns = [
            r"apolo\s+[\w-]+(?:\s+[\w-]+)*",  # apolo command subcommand
            r"`apolo[^`]+`",  # apolo commands in backticks
            r"```.*?apolo[^```]+```",  # apolo commands in code blocks
        ]
    
    def _determine_metadata(self, file_path: Path) -> DocumentMetadata:
        """Determine metadata for a documentation file based on its path and content"""
        
        relative_path = str(file_path.relative_to(self.docs_root))
        
        # Determine section and audience from path
        section = "unknown"
        audience = "user"
        content_type = "guide"
        
        for path_prefix, attrs in self.section_mapping.items():
            if relative_path.startswith(path_prefix):
                section = path_prefix.split("/")[-1]
                audience = attrs["audience"]
                content_type = attrs["content_type"]
                break
        
        # Extract title from filename or content
        title = file_path.stem.replace("-", " ").replace("_", " ").title()
        if title.lower() == "readme":
            title = f"{section.title()} Overview"
        
        # Determine subsection from intermediate directories
        path_parts = file_path.relative_to(self.docs_root).parts
        subsection = None
        if len(path_parts) > 2:  # More than just section/file.md
            subsection = path_parts[-2].replace("-", " ").replace("_", " ").title()
        
        return DocumentMetadata(
            file_path=str(file_path),
            relative_path=relative_path,
            title=title,
            section=section,
            subsection=subsection,
            audience=audience,
            content_type=content_type
        )
    
    def _extract_entities(self, content: str) -> List[str]:
        """Extract Apolo entity mentions from content"""
        entities_found = []
        content_lower = content.lower()
        
        for entity in self.apolo_entities:
            # Look for entity mentions in various forms
            patterns = [
                rf"\b{entity}\b",  # exact word
                rf"\b{entity}s?\b",  # plural forms
                rf"apolo\s+{entity}",  # apolo command context
            ]
            
            for pattern in patterns:
                if re.search(pattern, content_lower, re.IGNORECASE):
                    entities_found.append(entity)
                    break
        
        return list(set(entities_found))
    
    def _extract_cli_commands(self, content: str) -> List[str]:
        """Extract CLI commands from content"""
        commands = []
        
        for pattern in self.cli_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            for match in matches:
                # Clean up the command
                clean_command = re.sub(r'```[a-zA-Z]*\n?', '', match)
                clean_command = clean_command.strip('`').strip()
                if clean_command and len(clean_command) < 200:  # Reasonable command length
                    commands.append(clean_command)
        
        return list(set(commands))
    
    def _load_file_content(self, file_path: Path) -> str:
        """Load and clean file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic cleaning
            content = re.sub(r'\n{3,}', '\n\n', content)  # Reduce multiple newlines
            content = content.strip()
            
            return content
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            return ""
    
    def load_documentation(self) -> List[ProcessedDocument]:
        """
        Load all documentation files from the apolo-documentation directory
        """
        logger.info(f"Loading documentation from {self.docs_root}")
        
        if not self.docs_root.exists():
            raise FileNotFoundError(f"Documentation directory not found: {self.docs_root}")
        
        # Find all markdown files
        md_files = list(self.docs_root.rglob("*.md"))
        logger.info(f"Found {len(md_files)} markdown files")
        
        processed_docs = []
        
        for file_path in md_files:
            try:
                # Load content
                content = self._load_file_content(file_path)
                if not content:
                    continue
                
                # Extract metadata
                metadata = self._determine_metadata(file_path)
                
                # Extract entities and commands
                entities = self._extract_entities(content)
                commands = self._extract_cli_commands(content)
                
                # Create processed document
                doc = ProcessedDocument(
                    content=content,
                    metadata=metadata,
                    entities_mentioned=entities,
                    cli_commands=commands
                )
                
                processed_docs.append(doc)
                
                logger.debug(f"Processed {file_path.name}: {len(entities)} entities, {len(commands)} commands")
                
            except Exception as e:
                logger.error(f"Error processing file {file_path}: {e}")
                continue
        
        self.processed_docs = processed_docs
        logger.info(f"Successfully processed {len(processed_docs)} documentation files")
        
        return processed_docs
    
    def get_documents_by_section(self, section: str) -> List[ProcessedDocument]:
        """Get documents filtered by section"""
        return [doc for doc in self.processed_docs if doc.metadata.section == section]
    
    def get_documents_by_audience(self, audience: str) -> List[ProcessedDocument]:
        """Get documents filtered by audience"""
        return [doc for doc in self.processed_docs if doc.metadata.audience == audience]
    
    def get_statistics(self) -> Dict[str, int]:
        """Get loading statistics"""
        if not self.processed_docs:
            return {}
        
        stats = {
            "total_documents": len(self.processed_docs),
            "total_content_length": sum(len(doc.content) for doc in self.processed_docs),
            "avg_content_length": sum(len(doc.content) for doc in self.processed_docs) // len(self.processed_docs),
        }
        
        # Count by sections
        sections = {}
        audiences = {}
        content_types = {}
        
        for doc in self.processed_docs:
            sections[doc.metadata.section] = sections.get(doc.metadata.section, 0) + 1
            audiences[doc.metadata.audience] = audiences.get(doc.metadata.audience, 0) + 1
            content_types[doc.metadata.content_type] = content_types.get(doc.metadata.content_type, 0) + 1
        
        stats.update({
            "sections": sections,
            "audiences": audiences,
            "content_types": content_types
        })
        
        return stats


# CLI interface for testing
if __name__ == "__main__":
    import sys
    
    # Simple test
    loader = DocumentationLoader()
    docs = loader.load_documentation()
    
    print(f"Loaded {len(docs)} documents")
    
    stats = loader.get_statistics()
    print("Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Show sample document
    if docs:
        sample = docs[0]
        print(f"\nSample document: {sample.metadata.title}")
        print(f"Path: {sample.metadata.relative_path}")
        print(f"Section: {sample.metadata.section}")
        print(f"Audience: {sample.metadata.audience}")
        print(f"Entities: {sample.entities_mentioned}")
        print(f"Commands: {sample.cli_commands[:3]}...")  # First 3 commands
        print(f"Content preview: {sample.content[:200]}...")