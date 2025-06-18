#!/usr/bin/env python3
"""
Simplified script to load documentation into LightRAG
Loads all markdown files from a directory structure
"""

import asyncio
import httpx
import argparse
import sys
from pathlib import Path
from typing import List, Optional


async def load_document_to_lightrag(
    content: str, 
    title: str, 
    file_path: str,
    endpoint: str = "http://localhost:9621"
) -> bool:
    """Load a single document to LightRAG"""
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{endpoint}/documents/text",
                headers={"Content-Type": "application/json"},
                json={
                    "text": content,
                    "file_path": file_path
                }
            )
            
            if response.status_code == 200:
                print(f"✅ Loaded: {title}")
                return True
            else:
                print(f"❌ Failed to load {title}: {response.status_code}")
                if response.status_code == 500:
                    try:
                        error_detail = response.json()
                        print(f"   Error details: {error_detail}")
                    except:
                        print(f"   Response: {response.text}")
                return False
                
    except Exception as e:
        print(f"❌ Error loading {title}: {e}")
        return False


def load_markdown_files(docs_path: Path) -> List[tuple]:
    """Load all markdown files from directory structure"""
    if not docs_path.exists():
        raise FileNotFoundError(f"Documentation directory not found: {docs_path}")
    
    # Find all markdown files
    md_files = list(docs_path.rglob("*.md"))
    print(f"📚 Found {len(md_files)} markdown files")
    
    documents = []
    
    for file_path in md_files:
        try:
            # Load content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            if not content:
                continue
                
            # Generate title from filename
            title = file_path.stem.replace("-", " ").replace("_", " ").title()
            if title.lower() == "readme":
                # Use parent directory name for README files
                title = f"{file_path.parent.name.title()} Overview"
            
            # Get relative path for metadata
            relative_path = str(file_path.relative_to(docs_path))
            
            # Prepare content with basic metadata
            content_with_metadata = f"""
Title: {title}
Path: {relative_path}
Source: {file_path.name}

{content}
"""
            
            documents.append((content_with_metadata, title, relative_path))
            
        except Exception as e:
            print(f"⚠️ Error processing {file_path}: {e}")
            continue
    
    return documents


async def test_lightrag_health(endpoint: str = "http://localhost:9621") -> bool:
    """Test if LightRAG is accessible"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{endpoint}/health")
            if response.status_code == 200:
                health_data = response.json()
                print(f"✅ LightRAG is healthy: {health_data.get('status')}")
                return True
            else:
                print(f"❌ LightRAG health check failed: {response.status_code}")
                return False
    except Exception as e:
        print(f"❌ Cannot connect to LightRAG: {e}")
        return False


async def test_query(endpoint: str = "http://localhost:9621") -> None:
    """Test a sample query"""
    print(f"\n🧪 Testing query...")
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{endpoint}/query",
                headers={"Content-Type": "application/json"},
                json={"query": "What is this documentation about?", "mode": "hybrid"}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Query successful!")
                print(f"Response: {result['response'][:200]}...")
            else:
                print(f"❌ Query failed: {response.status_code}")
                
    except Exception as e:
        print(f"❌ Query error: {e}")


async def main():
    """Main loading function"""
    parser = argparse.ArgumentParser(
        description="Load documentation into LightRAG",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Load from relative path
  python load_docs.py ../apolo-copilot/docs/official-apolo-documentation/docs
  
  # Load from absolute path  
  python load_docs.py /path/to/documentation
  
  # Use custom endpoint
  python load_docs.py docs/ --endpoint https://lightrag.example.com
"""
    )
    
    parser.add_argument(
        "docs_path",
        nargs="?",
        default="../apolo-copilot/docs/official-apolo-documentation/docs",
        help="Path to documentation directory (default: ../apolo-copilot/docs/official-apolo-documentation/docs)"
    )
    parser.add_argument(
        "--endpoint",
        default="http://localhost:9621",
        help="LightRAG endpoint URL (default: http://localhost:9621)"
    )
    parser.add_argument(
        "--no-test",
        action="store_true",
        help="Skip test query after loading"
    )
    
    args = parser.parse_args()
    
    print("🚀 Loading Documentation into LightRAG")
    print("=" * 60)
    print(f"📁 Documentation path: {args.docs_path}")
    print(f"🌐 LightRAG endpoint: {args.endpoint}")
    print()
    
    # Test LightRAG connectivity
    if not await test_lightrag_health(args.endpoint):
        print("❌ Cannot connect to LightRAG. Please ensure it's running and accessible.")
        sys.exit(1)
    
    # Load documents
    docs_path = Path(args.docs_path).resolve()
    try:
        documents = load_markdown_files(docs_path)
    except FileNotFoundError as e:
        print(f"❌ {e}")
        sys.exit(1)
    
    if not documents:
        print("❌ No markdown files found to load")
        sys.exit(1)
    
    # Calculate statistics
    total_content = sum(len(content) for content, _, _ in documents)
    avg_content = total_content // len(documents) if documents else 0
    
    print(f"📊 Total content: {total_content:,} characters")
    print(f"📊 Average length: {avg_content:,} characters")
    
    # Load documents
    successful = 0
    failed = 0
    
    print(f"\n🔄 Starting to load documents...")
    
    for i, (content, title, file_path) in enumerate(documents):
        success = await load_document_to_lightrag(content, title, file_path, args.endpoint)
        
        if success:
            successful += 1
        else:
            failed += 1
        
        # Progress update
        if (i + 1) % 10 == 0:
            print(f"📈 Progress: {i + 1}/{len(documents)} ({successful} success, {failed} failed)")
        
        # Small delay to avoid overwhelming the service
        await asyncio.sleep(0.3)
    
    print(f"\n✅ Loading complete!")
    print(f"📊 Successful: {successful}")
    print(f"📊 Failed: {failed}")
    
    # Test query unless disabled
    if not args.no_test and successful > 0:
        await test_query(args.endpoint)


if __name__ == "__main__":
    asyncio.run(main())