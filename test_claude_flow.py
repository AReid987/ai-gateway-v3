#!/usr/bin/env python3
"""
Test Claude Flow Hive and Swarm with AI Gateway
"""
import asyncio
from claude_flow_hive import create_research_hive
from claude_flow_swarm import Swarm, demo_swarm
from gateway_client import GatewayFactory

async def test_gateway_client():
    """Test basic gateway connectivity"""
    print("🔌 Testing AI Gateway connection...")
    client = GatewayFactory.balanced()
    
    try:
        response = client.chat_completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=20
        )
        print(f"✅ Gateway connected: {response['choices'][0]['message']['content']}")
        return True
    except Exception as e:
        print(f"❌ Gateway connection failed: {e}")
        return False

async def test_hive():
    """Test hive functionality"""
    print("\n🐝 Testing Hive...")
    hive = create_research_hive()
    
    try:
        results = await hive.collaborate("What is artificial intelligence?")
        print("✅ Hive collaboration successful:")
        for agent, result in results.items():
            print(f"  {agent}: {result[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Hive test failed: {e}")
        return False

async def test_swarm():
    """Test swarm functionality"""
    print("\n🐛 Testing Swarm...")
    
    try:
        results = await demo_swarm()
        print("✅ Swarm mission successful:")
        print(f"  Mission: {results['mission']}")
        print(f"  Teams involved: {list(results['results'].keys())}")
        return True
    except Exception as e:
        print(f"❌ Swarm test failed: {e}")
        return False

async def main():
    print("🚀 Claude Flow + AI Gateway v2 Test Suite")
    print("=" * 50)
    
    # Test gateway
    gateway_ok = await test_gateway_client()
    if not gateway_ok:
        print("\n❌ Gateway not available. Start with: cd ai-gateway && ./target/release/ai-gateway --config config.yaml")
        return
    
    # Test hive
    await test_hive()
    
    # Test swarm
    await test_swarm()
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    asyncio.run(main())
