#!/usr/bin/env python3
"""
Apolo Copilot - Main CLI interface
"""

import asyncio
import httpx
import sys
from pathlib import Path

# Add current directory to path for imports when run as script
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))


class ApoloCopilot:
    """Simple Apolo Copilot CLI interface"""
    
    def __init__(self, lightrag_url: str = "http://localhost:9621"):
        self.lightrag_url = lightrag_url.rstrip('/')
        
    async def health_check(self) -> bool:
        """Check if LightRAG is available"""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{self.lightrag_url}/health")
                return response.status_code == 200
        except Exception:
            return False
    
    async def query(self, query: str, mode: str = "hybrid") -> str:
        """Query LightRAG and return response"""
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.lightrag_url}/query",
                    headers={"Content-Type": "application/json"},
                    json={"query": query, "mode": mode}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return result.get("response", "No response received")
                else:
                    return f"Query failed: {response.status_code} - {response.text}"
                    
        except Exception as e:
            return f"Error: {e}"
    
    def print_welcome(self):
        """Print welcome message"""
        print("🤖 Apolo Copilot - Your Intelligent Apolo Assistant")
        print("=" * 60)
        print("Ask me anything about the Apolo platform!")
        print("Commands:")
        print("  • Just type your question and press Enter")
        print("  • /help - Show this help")
        print("  • /mode <local|global|hybrid> - Change query mode")
        print("  • /exit or /quit - Exit the copilot")
        print("=" * 60)
        
    async def interactive_mode(self):
        """Run interactive CLI mode"""
        # Check health first
        print("🔍 Checking LightRAG connection...")
        if not await self.health_check():
            print("❌ LightRAG service is not available at " + self.lightrag_url)
            print("   Make sure docker-compose.minimal.yml is running")
            return
        
        print("✅ Connected to LightRAG")
        
        self.print_welcome()
        
        current_mode = "hybrid"
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n[{current_mode}] 🤔 Your question: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    command = user_input.lower()
                    
                    if command in ['/exit', '/quit']:
                        print("👋 Goodbye! Happy building with Apolo!")
                        break
                    
                    elif command == '/help':
                        self.print_welcome()
                        continue
                    
                    elif command.startswith('/mode '):
                        new_mode = command.split(' ', 1)[1].strip()
                        if new_mode in ['local', 'global', 'hybrid']:
                            current_mode = new_mode
                            print(f"✅ Query mode changed to: {current_mode}")
                        else:
                            print("❌ Invalid mode. Use: local, global, or hybrid")
                        continue
                    
                    else:
                        print(f"❌ Unknown command: {command}")
                        continue
                
                # Process query
                print("🔍 Searching Apolo documentation...")
                response = await self.query(user_input, current_mode)
                
                print(f"\n🤖 Apolo Copilot:")
                print("-" * 40)
                print(response)
                print("-" * 40)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Happy building with Apolo!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


async def main():
    """Main function"""
    copilot = ApoloCopilot()
    
    if len(sys.argv) > 1:
        # Command line query mode
        query = " ".join(sys.argv[1:])
        
        if not await copilot.health_check():
            print("❌ LightRAG service is not available")
            return
        
        print(f"🤔 Query: {query}")
        print("🔍 Searching...")
        
        response = await copilot.query(query)
        print(f"\n🤖 Response:\n{response}")
        
    else:
        # Interactive mode
        await copilot.interactive_mode()


if __name__ == "__main__":
    asyncio.run(main())