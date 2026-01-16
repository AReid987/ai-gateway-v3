#!/usr/bin/env python3
"""
Comprehensive test for Claude Flow integration with AI Gateway v3
Tests all components: gateway client, integration, hive, and swarm patterns
"""
import sys
import asyncio
from pathlib import Path

# Add packages to path
gateway_client_path = Path(__file__).parent / "packages" / "gateway-client" / "src"
claude_flow_path = Path(__file__).parent / "packages" / "claude-flow" / "src"
sys.path.insert(0, str(gateway_client_path))
sys.path.insert(0, str(claude_flow_path))

import requests
from gateway_client import GatewayFactory, AIGatewayClient
from integration import claude_flow_completion, claude_flow_chat
from hive import Hive, Agent, create_research_hive
from swarm import Swarm

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_gateway_connection():
    """Test 1: Verify gateway is running and accessible"""
    print_section("TEST 1: Gateway Connection")
    
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        if response.status_code == 200:
            print("✅ Gateway is running and healthy")
            return True
        else:
            print(f"❌ Gateway returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to gateway on port 8080")
        print("\n💡 To start the gateway:")
        print("   cd ai-gateway")
        print("   source ~/.zsh_secrets")
        print("   ./target/release/ai-gateway --config config.yaml")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_gateway_client():
    """Test 2: Test the gateway client package"""
    print_section("TEST 2: Gateway Client Package")
    
    try:
        # Test balanced client
        print("\n🔄 Testing balanced routing client...")
        client = GatewayFactory.balanced()
        response = client.chat_completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'Client working!' and nothing else."}],
            max_tokens=20
        )
        content = response['choices'][0]['message']['content']
        print(f"✅ Balanced client works: {content}")
        
        # Test fast client
        print("\n🔄 Testing fast routing client...")
        fast_client = GatewayFactory.fast()
        response = fast_client.chat_completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'Fast client working!' and nothing else."}],
            max_tokens=20
        )
        content = response['choices'][0]['message']['content']
        print(f"✅ Fast client works: {content}")
        
        return True
        
    except Exception as e:
        print(f"❌ Gateway client test failed: {e}")
        return False

def test_claude_flow_integration():
    """Test 3: Test Claude Flow integration functions"""
    print_section("TEST 3: Claude Flow Integration")
    
    try:
        # Test completion
        print("\n🔄 Testing claude_flow_completion...")
        result = claude_flow_completion(
            "Say 'Integration working!' and nothing else.",
            model="claude-3-haiku"
        )
        print(f"✅ Completion works: {result}")
        
        # Test chat
        print("\n🔄 Testing claude_flow_chat...")
        messages = [
            {"role": "user", "content": "Say 'Chat working!' and nothing else."}
        ]
        result = claude_flow_chat(messages, model="claude-3-haiku")
        print(f"✅ Chat works: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Claude Flow integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_hive_pattern():
    """Test 4: Test Hive pattern (multi-agent collaboration)"""
    print_section("TEST 4: Hive Pattern (Multi-Agent)")
    
    try:
        print("\n🔄 Creating a simple hive...")
        hive = Hive("test-hive")
        
        # Add agents
        hive.add_agent("agent1", "a helpful assistant", "groq/llama-3.1-8b-instant")
        hive.add_agent("agent2", "a creative thinker", "groq/llama-3.1-8b-instant")
        
        print(f"✅ Created hive with {len(hive.agents)} agents")
        
        # Test collaboration
        print("\n🔄 Testing agent collaboration...")
        task = "In one sentence, what is AI?"
        results = await hive.collaborate(task)
        
        print("✅ Hive collaboration successful!")
        for agent_name, result in results.items():
            print(f"\n   {agent_name}: {result[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Hive pattern test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_swarm_pattern():
    """Test 5: Test Swarm pattern (coordinated hives)"""
    print_section("TEST 5: Swarm Pattern (Coordinated Hives)")
    
    try:
        print("\n🔄 Creating a swarm with multiple hives...")
        swarm = Swarm("test-swarm")
        
        # Create and add first hive
        hive1 = Hive("analysis-team")
        hive1.add_agent("analyst", "a data analyst", "groq/llama-3.1-8b-instant")
        swarm.add_hive(hive1)
        
        # Create and add second hive
        hive2 = Hive("creative-team")
        hive2.add_agent("writer", "a creative writer", "groq/llama-3.1-8b-instant")
        swarm.add_hive(hive2)
        
        print(f"✅ Created swarm with {len(swarm.hives)} hives")
        
        # Test mission execution
        print("\n🔄 Testing swarm mission execution...")
        mission = "Explain quantum computing in simple terms"
        results = await swarm.execute_mission(mission)
        
        print("✅ Swarm mission successful!")
        print(f"\n   Mission: {results['mission']}")
        print(f"   Coordination: {results['coordination'][:100]}...")
        print(f"   Teams involved: {list(results['results'].keys())}")
        
        return True
        
    except Exception as e:
        print(f"❌ Swarm pattern test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_research_hive():
    """Test 6: Test pre-configured research hive"""
    print_section("TEST 6: Research Hive (Pre-configured)")
    
    try:
        print("\n🔄 Creating research hive...")
        hive = create_research_hive()
        
        print(f"✅ Research hive created with {len(hive.agents)} agents:")
        for agent in hive.agents:
            print(f"   - {agent.name}: {agent.role}")
        
        # Test research task
        print("\n🔄 Testing research collaboration...")
        task = "What are the key benefits of AI?"
        results = await hive.collaborate(task)
        
        print("✅ Research hive collaboration successful!")
        for agent_name, result in results.items():
            print(f"\n   {agent_name}:")
            print(f"   {result[:150]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Research hive test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def run_all_tests():
    """Run all tests in sequence"""
    print("\n" + "🚀" * 35)
    print("  AI GATEWAY v3 - CLAUDE FLOW INTEGRATION TEST SUITE")
    print("🚀" * 35)
    
    results = {}
    
    # Test 1: Gateway connection
    results['gateway_connection'] = test_gateway_connection()
    if not results['gateway_connection']:
        print("\n❌ Gateway is not running. Please start it first.")
        print("   See START_GATEWAY.md for instructions.")
        return results
    
    # Test 2: Gateway client
    results['gateway_client'] = test_gateway_client()
    
    # Test 3: Claude Flow integration
    results['claude_flow_integration'] = test_claude_flow_integration()
    
    # Test 4: Hive pattern
    results['hive_pattern'] = await test_hive_pattern()
    
    # Test 5: Swarm pattern
    results['swarm_pattern'] = await test_swarm_pattern()
    
    # Test 6: Research hive
    results['research_hive'] = await test_research_hive()
    
    # Print summary
    print_section("TEST SUMMARY")
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    
    print(f"\nTotal Tests: {total}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    print("\nDetailed Results:")
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name.replace('_', ' ').title()}")
    
    if failed == 0:
        print("\n" + "🎉" * 35)
        print("  ALL TESTS PASSED! Claude Flow integration is working!")
        print("🎉" * 35)
    else:
        print("\n" + "⚠️ " * 35)
        print(f"  {failed} test(s) failed. Check the output above for details.")
        print("⚠️ " * 35)
    
    return results

def main():
    """Main entry point"""
    try:
        results = asyncio.run(run_all_tests())
        
        # Exit with error code if any tests failed
        if not all(results.values()):
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

