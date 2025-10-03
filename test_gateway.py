import requests
import os
import json

# Load API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Gateway endpoint
base_url = "http://localhost:8585"

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_models():
    """Test the models endpoint"""
    try:
        response = requests.get(f"{base_url}/v1/models")
        print(f"Models endpoint: {response.status_code}")
        if response.status_code == 200:
            models = response.json()
            print(f"Available models: {len(models['data'])}")
            for model in models['data'][:3]:  # Show first 3
                print(f"  - {model['id']} ({model['provider']})")
        return response.status_code == 200
    except Exception as e:
        print(f"Models test failed: {e}")
        return False

def test_chat_completion(model="gpt-3.5-turbo"):
    """Test chat completion with specified model"""
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": "Hello! This is a test. Please respond with just 'Gateway working!'"
            }
        ],
        "max_tokens": 10
    }

    try:
        print(f"\nTesting {model}...")
        response = requests.post(
            f"{base_url}/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print(f"✅ Success! Response: {message}")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=== AI Gateway Test Suite ===\n")
    
    # Test health
    if not test_health():
        print("Gateway is not healthy, stopping tests")
        return
    
    # Test models endpoint
    test_models()
    
    # Test different models
    models_to_test = [
        "gpt-3.5-turbo",
        "claude-3-haiku-20240307", 
        "gemini-pro",
        "llama-3.1-70b-versatile"
    ]
    
    results = {}
    for model in models_to_test:
        results[model] = test_chat_completion(model)
    
    print(f"\n=== Test Results ===")
    for model, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{model}: {status}")

if __name__ == "__main__":
    main()
