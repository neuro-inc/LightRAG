"""
LightRAG client for interacting with the deployed LightRAG instance
"""

import asyncio
import httpx
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

from ..data.loader import ProcessedDocument

logger = logging.getLogger(__name__)


@dataclass
class QueryResult:
    """Result from a LightRAG query"""
    response: str
    query: str
    mode: str
    sources: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


class LightRAGClient:
    """
    Client for interacting with the deployed LightRAG instance.
    
    Handles document insertion and retrieval operations.
    """
    
    def __init__(self, api_url: str = "http://localhost:9621", api_key: Optional[str] = None):
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.client = httpx.AsyncClient(timeout=30.0)
        
        # Default headers
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
    
    async def health_check(self) -> bool:
        """Check if LightRAG service is healthy"""
        try:
            response = await self.client.get(f"{self.api_url}/health")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False
    
    async def insert_document(self, document: ProcessedDocument) -> bool:
        """
        Insert a processed document into LightRAG
        """
        try:
            # Prepare document text with metadata
            document_text = self._prepare_document_for_insertion(document)
            
            payload = {"text": document_text}
            
            response = await self.client.post(
                f"{self.api_url}/documents/text",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                logger.debug(f"Inserted document: {document.metadata.title}")
                return True
            else:
                logger.error(f"Failed to insert document {document.metadata.title}: {response.status_code} {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error inserting document {document.metadata.title}: {e}")
            return False
    
    async def insert_documents_batch(self, documents: List[ProcessedDocument]) -> Dict[str, int]:
        """
        Insert multiple documents in batch
        """
        results = {"success": 0, "failed": 0}
        
        logger.info(f"Inserting {len(documents)} documents...")
        
        for i, document in enumerate(documents):
            try:
                success = await self.insert_document(document)
                if success:
                    results["success"] += 1
                else:
                    results["failed"] += 1
                    
                # Progress logging
                if (i + 1) % 10 == 0:
                    logger.info(f"Processed {i + 1}/{len(documents)} documents")
                    
                # Small delay to avoid overwhelming the service
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"Error processing document {i}: {e}")
                results["failed"] += 1
        
        logger.info(f"Batch insertion complete: {results['success']} success, {results['failed']} failed")
        return results
    
    async def query(self, 
                   query: str, 
                   mode: str = "hybrid",
                   **kwargs) -> QueryResult:
        """
        Query LightRAG with the given query
        
        Args:
            query: The query string
            mode: Query mode (local, global, hybrid)
            **kwargs: Additional query parameters
        """
        try:
            payload = {
                "query": query,
                "mode": mode,
                **kwargs
            }
            
            response = await self.client.post(
                f"{self.api_url}/query",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                return QueryResult(
                    response=result.get("response", ""),
                    query=query,
                    mode=mode,
                    metadata=result
                )
            else:
                logger.error(f"Query failed: {response.status_code} {response.text}")
                return QueryResult(
                    response=f"Query failed: {response.status_code}",
                    query=query,
                    mode=mode
                )
                
        except Exception as e:
            logger.error(f"Error querying LightRAG: {e}")
            return QueryResult(
                response=f"Error: {str(e)}",
                query=query,
                mode=mode
            )
    
    async def get_pipeline_status(self) -> Dict[str, Any]:
        """Get the current pipeline processing status"""
        try:
            response = await self.client.get(f"{self.api_url}/documents/pipeline_status")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Status check failed: {response.status_code}"}
        except Exception as e:
            logger.error(f"Error getting pipeline status: {e}")
            return {"error": str(e)}
    
    async def wait_for_processing(self, timeout: int = 300) -> bool:
        """
        Wait for document processing to complete
        
        Args:
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if processing completed, False if timeout
        """
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status = await self.get_pipeline_status()
            
            if not status.get("busy", False):
                logger.info("Document processing completed")
                return True
            
            logger.info("Document processing in progress...")
            await asyncio.sleep(5)
        
        logger.warning("Timeout waiting for document processing")
        return False
    
    def _prepare_document_for_insertion(self, document: ProcessedDocument) -> str:
        """
        Prepare document content with metadata for LightRAG insertion.
        
        This enriches the document with metadata that can help with
        entity extraction and relationship identification.
        """
        
        # Start with metadata header
        metadata_header = f"""
Document: {document.metadata.title}
Path: {document.metadata.relative_path}
Section: {document.metadata.section}
Audience: {document.metadata.audience}
Content Type: {document.metadata.content_type}
"""
        
        if document.metadata.subsection:
            metadata_header += f"Subsection: {document.metadata.subsection}\n"
        
        # Add entity context if entities are mentioned
        if document.entities_mentioned:
            metadata_header += f"Apolo Entities: {', '.join(document.entities_mentioned)}\n"
        
        # Add CLI commands context if commands are present
        if document.cli_commands:
            metadata_header += f"CLI Commands: {len(document.cli_commands)} commands found\n"
        
        metadata_header += "\n---\n\n"
        
        # Combine metadata with content
        enriched_content = metadata_header + document.content
        
        # Add CLI commands section if present
        if document.cli_commands:
            commands_section = "\n\n--- CLI Commands Referenced ---\n"
            for cmd in document.cli_commands[:10]:  # Limit to first 10 commands
                commands_section += f"- {cmd}\n"
            enriched_content += commands_section
        
        return enriched_content
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()


# Async context manager support
class AsyncLightRAGClient(LightRAGClient):
    """Async context manager version of LightRAGClient"""
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


# CLI interface for testing
if __name__ == "__main__":
    import asyncio
    import sys
    from pathlib import Path
    
    # Add parent directory to path for imports
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    from data.loader import DocumentationLoader
    
    async def test_client():
        """Test the LightRAG client"""
        
        async with AsyncLightRAGClient() as client:
            # Test health check
            health = await client.health_check()
            print(f"LightRAG health: {'✅ OK' if health else '❌ Failed'}")
            
            if not health:
                print("LightRAG service is not available")
                return
            
            # Test query
            result = await client.query("What is Apolo?")
            print(f"Query result: {result.response[:200]}...")
            
            # Test pipeline status
            status = await client.get_pipeline_status()
            print(f"Pipeline status: {status}")
    
    # Run test
    asyncio.run(test_client())