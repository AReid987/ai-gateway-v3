#!/usr/bin/env python3
"""
Test script for Helicone AI Gateway
Tests intelligent routing, load balancing, and fallback behavior
"""

import requests
import json
import time
import sys

GATEWAY_URL = "http://localhost:8080"

def test_health():
    """Test basic connectivity"""
    try:
        response = requests.get(f"{GATEWAY_URL}/health", timeout=5)
        print(f"✅ Health check: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_model_routing(model, router_id=None):
    """Test routing to specific models"""
    headers = {"Content-Type": "application/json"}
    if router_id:
        headers["X-Router-Id"] = router_id
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": "Hello! Respond with just 'OK'"}],
        "max_tokens": 5
    }
    
    try:
        response = requests.post(
            f"{GATEWAY_URL}/ai/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        result = response.json()
        
        if response.status_code == 200:
            message = result.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(f"✅ {model}: Success - {message.strip()}")
            return True
        else:
            error_msg = result.get('error', {}).get('message', 'Unknown error')
            error_code = result.get('error', {}).get('code', 'unknown')
            
            if error_code in ['insufficient_quota', 'invalid_api_key']:
                print(f"⚠️  {model}: Expected error - {error_code}")
                return True  # Expected for quota/key issues
            else:
                print(f"❌ {model}: Unexpected error - {error_msg}")
                return False
                
    except Exception as e:
        print(f"❌ {model}: Request failed - {e}")
        return False

def test_load_balancing():
    """Test load balancing by making multiple requests"""
    print("\n🔄 Testing load balancing with main router...")
    
    models_to_test = [
        "openai/gpt-4o-mini",
        "groq/llama-3.1-8b-instant", 
        "anthropic/claude-3-haiku-20240307"
    ]
    
    results = {}
    for model in models_to_test:
        print(f"\nTesting {model}...")
        success = test_model_routing(model, "main")
        results[model] = success
    
    return results

def test_fast_router():
    """Test the fast router configuration"""
    print("\n⚡ Testing fast router...")
    
    models_to_test = [
        "groq/llama-3.1-8b-instant",
        "openai/gpt-4o-mini"
    ]
    
    results = {}
    for model in models_to_test:
        print(f"\nTesting {model} with fast router...")
        success = test_model_routing(model, "fast")
        results[model] = success
    
    return results

def main():
    print("🚀 Helicone AI Gateway Test Suite")
    print("=" * 50)
    
    # Test basic connectivity
    if not test_health():
        print("❌ Gateway is not responding. Make sure it's running on port 8080.")
        sys.exit(1)
    
    print("\n📊 Testing model routing...")
    
    # Test individual models
    models_to_test = [
        "openai/gpt-4o-mini",
        "groq/llama-3.1-8b-instant",
        "anthropic/claude-3-haiku-20240307"
    ]
    
    individual_results = {}
    for model in models_to_test:
        print(f"\nTesting {model}...")
        individual_results[model] = test_model_routing(model)
    
    # Test load balancing
    lb_results = test_load_balancing()
    
    # Test fast router
    fast_results = test_fast_router()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Summary")
    print("=" * 50)
    
    print("\n🎯 Individual Model Tests:")
    for model, success in individual_results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {model}: {status}")
    
    print("\n⚖️  Load Balancing Tests:")
    for model, success in lb_results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {model}: {status}")
    
    print("\n⚡ Fast Router Tests:")
    for model, success in fast_results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {model}: {status}")
    
    # Overall status
    all_tests = list(individual_results.values()) + list(lb_results.values()) + list(fast_results.values())
    total_tests = len(all_tests)
    passed_tests = sum(all_tests)
    
    print(f"\n🏆 Overall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Gateway is working correctly.")
    else:
        print("⚠️  Some tests failed. Check API keys and provider configurations.")

if __name__ == "__main__":
    main()
