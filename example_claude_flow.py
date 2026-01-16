#!/usr/bin/env python3
"""
Simple Claude Flow Example with AI Gateway

This script demonstrates how to use Claude Flow patterns with the AI Gateway.
Make sure the gateway is running before executing this script!

Usage:
    1. Start gateway: cd apps/ai-gateway && ./target/release/ai-gateway --config config.yaml
    2. Activate venv: source .venv/bin/activate
    3. Run script: python example_claude_flow.py
"""

import sys
from gateway_client import AIGatewayClient, GatewayFactory

def test_gateway_connection():
    """Test if gateway is accessible"""
    print("🔍 Testing gateway connection...")
    try:
        import requests
        response = requests.get("http://localhost:8080/health", timeout=2)
        if response.status_code == 200:
            print("✅ Gateway is running!")
            return True
        else:
            print(f"❌ Gateway returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to gateway: {e}")
        print("\n💡 Make sure gateway is running:")
        print("   cd apps/ai-gateway")
        print("   ./target/release/ai-gateway --config config.yaml")
        return False

def example_1_simple_request():
    """Example 1: Simple chat completion request"""
    print("\n" + "="*60)
    print("Example 1: Simple Chat Completion")
    print("="*60)
    
    # Create gateway client
    client = AIGatewayClient(base_url="http://localhost:8080")
    
    # Send request
    print("📤 Sending request to gateway...")
    try:
        response = client.chat_completion(
            model="llama-3.3-70b-versatile",  # Groq model
            messages=[
                {"role": "user", "content": "In one sentence, what is an AI gateway?"}
            ]
        )
        
        # Print response
        print("📥 Response received:")
        print(response['choices'][0]['message']['content'])
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def example_2_hive_pattern():
    """Example 2: Multi-agent Hive pattern"""
    print("\n" + "="*60)
    print("Example 2: Multi-Agent Hive Pattern")
    print("="*60)
    
    try:
        from hive import Hive, Agent
        
        # Create gateway client
        gateway = GatewayFactory.balanced()
        
        # Create agents
        print("🤖 Creating agents...")
        researcher = Agent(
            name="Researcher",
            role="Research and gather information about topics",
            gateway_client=gateway
        )
        
        writer = Agent(
            name="Writer",
            role="Write clear and concise summaries",
            gateway_client=gateway
        )
        
        # Create hive
        print("🐝 Creating hive with 2 agents...")
        hive = Hive(
            name="Research & Writing Hive",
            agents=[researcher, writer],
            gateway_client=gateway
        )
        
        # Run task
        print("🚀 Running collaborative task...")
        task = "Explain what load balancing is in 2 sentences"
        result = hive.run(task)
        
        print("📥 Hive result:")
        print(result)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def example_3_swarm_pattern():
    """Example 3: Coordinated Swarm pattern"""
    print("\n" + "="*60)
    print("Example 3: Coordinated Swarm Pattern")
    print("="*60)
    
    try:
        from swarm import Swarm
        from hive import Hive, Agent
        
        # Create gateway client
        gateway = GatewayFactory.balanced()
        
        # Create first hive (Analysis)
        print("🐝 Creating Analysis Hive...")
        analysis_hive = Hive(
            name="Analysis Team",
            agents=[
                Agent("Analyst", "Analyze problems and identify key points", gateway)
            ],
            gateway_client=gateway
        )
        
        # Create second hive (Solutions)
        print("🐝 Creating Solutions Hive...")
        solutions_hive = Hive(
            name="Solutions Team",
            agents=[
                Agent("Problem Solver", "Propose practical solutions", gateway)
            ],
            gateway_client=gateway
        )
        
        # Create swarm
        print("🌐 Creating swarm with 2 hives...")
        swarm = Swarm(
            name="Problem-Solving Swarm",
            hives=[analysis_hive, solutions_hive],
            gateway_client=gateway
        )
        
        # Run coordinated task
        print("🚀 Running coordinated task across hives...")
        task = "How can we make API requests faster?"
        result = swarm.run(task)
        
        print("📥 Swarm result:")
        print(result)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def example_4_different_models():
    """Example 4: Using different models"""
    print("\n" + "="*60)
    print("Example 4: Using Different Models")
    print("="*60)
    
    client = AIGatewayClient(base_url="http://localhost:8080")
    
    models = [
        "llama-3.3-70b-versatile",  # Groq - Large model
        "llama-3.1-8b-instant",     # Groq - Fast model
    ]
    
    question = "What is 2+2?"
    
    for model in models:
        print(f"\n🤖 Testing model: {model}")
        try:
            response = client.chat_completion(
                model=model,
                messages=[{"role": "user", "content": question}]
            )
            answer = response['choices'][0]['message']['content']
            print(f"   Answer: {answer[:100]}...")
        except Exception as e:
            print(f"   ❌ Error: {e}")

def main():
    """Run all examples"""
    print("🚀 Claude Flow Examples with AI Gateway")
    print("="*60)
    
    # Test gateway connection first
    if not test_gateway_connection():
        print("\n❌ Cannot proceed without gateway running.")
        print("\n📝 To start the gateway:")
        print("   1. Open a new terminal")
        print("   2. cd apps/ai-gateway")
        print("   3. source ~/.zsh_secrets")
        print("   4. ./target/release/ai-gateway --config config.yaml")
        sys.exit(1)
    
    # Run examples
    examples = [
        ("Simple Request", example_1_simple_request),
        ("Hive Pattern", example_2_hive_pattern),
        ("Swarm Pattern", example_3_swarm_pattern),
        ("Different Models", example_4_different_models),
    ]
    
    results = {}
    for name, func in examples:
        try:
            results[name] = func()
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error in {name}: {e}")
            results[name] = False
    
    # Summary
    print("\n" + "="*60)
    print("📊 Summary")
    print("="*60)
    for name, success in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {name}")
    
    print("\n✨ Done! Check out CLAUDE_FLOW_QUICKSTART.md for more examples.")

if __name__ == "__main__":
    main()

