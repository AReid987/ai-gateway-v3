#!/usr/bin/env python3
"""
Simple test to verify the AI Gateway is working
"""
import sys
from pathlib import Path

# Add gateway-client package to path
gateway_client_path = Path(__file__).parent / "packages" / "gateway-client" / "src"
sys.path.insert(0, str(gateway_client_path))

from gateway_client import GatewayFactory
import requests

def test_health():
    """Test gateway health endpoint"""
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        if response.status_code == 200:
            print("✅ Gateway is healthy!")
            return True
        else:
            print(f"❌ Gateway health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to gateway. Is it running on port 8080?")
        print("\nTo start the gateway:")
        print("  cd ai-gateway")
        print("  source ~/.zsh_secrets")
        print("  ./target/release/ai-gateway --config config.yaml")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_chat_completion():
    """Test chat completion through gateway client"""
    try:
        client = GatewayFactory.balanced()
        
        print("\n🔄 Testing chat completion...")
        response = client.chat_completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'Gateway working!' and nothing else."}],
            max_tokens=20
        )
        
        content = response['choices'][0]['message']['content']
        print(f"✅ Chat completion successful!")
        print(f"   Response: {content}")
        return True
        
    except Exception as e:
        print(f"❌ Chat completion failed: {e}")
        return False

def main():
    print("=" * 60)
    print("AI Gateway v3 - Simple Test")
    print("=" * 60)
    
    # Test health
    if not test_health():
        sys.exit(1)
    
    # Test chat completion
    if not test_chat_completion():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

