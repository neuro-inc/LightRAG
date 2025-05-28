#!/usr/bin/env python3
"""
Simple script to load Apolo documentation into LightRAG
"""

import asyncio
import httpx
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path("src").resolve()))

from data.loader import DocumentationLoader


async def load_document_to_lightrag(content: str, title: str) -> bool:
    """Load a single document to LightRAG"""
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "http://localhost:9621/documents/text",
                headers={"Content-Type": "application/json"},
                json={"text": content}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Loaded: {title}")
                return True
            else:
                print(f"❌ Failed to load {title}: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"❌ Error loading {title}: {e}")
        return False


async def main():
    """Main loading function"""
    print("🚀 Loading Apolo Documentation into LightRAG")
    print("=" * 60)
    
    # Load documents
    loader = DocumentationLoader()
    docs = loader.load_documentation()
    
    print(f"📚 Found {len(docs)} documents to load")
    
    # Show statistics
    stats = loader.get_statistics()
    print(f"📊 Total content: {stats['total_content_length']:,} characters")
    print(f"📊 Average length: {stats['avg_content_length']:,} characters")
    
    # Load documents
    successful = 0
    failed = 0
    
    print(f"\n🔄 Starting to load documents...")
    
    for i, doc in enumerate(docs):
        # Prepare content with metadata
        content_with_metadata = f"""
Title: {doc.metadata.title}
Section: {doc.metadata.section}
Path: {doc.metadata.relative_path}
Audience: {doc.metadata.audience}
Type: {doc.metadata.content_type}

{doc.content}
"""
        
        success = await load_document_to_lightrag(content_with_metadata, doc.metadata.title)
        
        if success:
            successful += 1
        else:
            failed += 1
        
        # Progress update
        if (i + 1) % 10 == 0:
            print(f"📈 Progress: {i + 1}/{len(docs)} ({successful} success, {failed} failed)")
        
        # Small delay to avoid overwhelming the service
        await asyncio.sleep(0.5)
    
    print(f"\n✅ Loading complete!")
    print(f"📊 Successful: {successful}")
    print(f"📊 Failed: {failed}")
    
    # Test a query
    print(f"\n🧪 Testing query...")
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "http://localhost:9621/query",
                headers={"Content-Type": "application/json"},
                json={"query": "What is Apolo platform?", "mode": "hybrid"}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Query successful!")
                print(f"Response: {result['response'][:300]}...")
            else:
                print(f"❌ Query failed: {response.status_code}")
                
    except Exception as e:
        print(f"❌ Query error: {e}")


if __name__ == "__main__":
    asyncio.run(main())