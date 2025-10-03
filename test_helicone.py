import requests
import os

# Load API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HELICONE_API_KEY = os.getenv("HELICONE_API_KEY")

# For local self-hosted gateway
base_url = "http://localhost:8585/v1"

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Helicone-Auth": f"Bearer {HELICONE_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello, world! This is a test event to unblock the Helicone wizard."
        }
    ],
    "max_tokens": 50
}

try:
    print("Sending test event to Helicone gateway...")
    print(f"Using OpenAI API key: {OPENAI_API_KEY[:20]}...")
    print(f"Using Helicone API key: {HELICONE_API_KEY[:20]}...")

    response = requests.post(
        f"{base_url}/chat/completions",
        headers=headers,
        json=data,
        timeout=30
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 200:
        print("✅ Success! Event sent successfully to Helicone gateway.")
    else:
        print(f"❌ Failed with status code: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"❌ Error sending request: {e}")