#!/usr/bin/env python3
"""
Dynamic model discovery for AI Gateway
Checks providers for free/available models and updates configuration
"""

import requests
import yaml
import json
import os
from datetime import datetime

def discover_groq_models():
    """Get models from Groq"""
    try:
        response = requests.get(
            "https://api.groq.com/openai/v1/models",
            headers={"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"},
            timeout=10
        )
        if response.status_code == 200:
            models = response.json().get('data', [])
            return [f"groq/{m['id']}" for m in models if 'llama' in m['id'].lower()]
    except Exception as e:
        print(f"Groq discovery failed: {e}")
    return ["groq/llama-3.1-8b-instant", "groq/llama-3.1-70b-versatile"]

def get_available_models():
    """Get all available models from supported providers"""
    models = {
        "groq": discover_groq_models(),
        "gemini": ["gemini/gemini-2.0-flash", "gemini/gemini-1.5-flash", "gemini/gemini-1.5-pro"],
        "mistral": ["mistral/mistral-small", "mistral/codestral-mamba"],
        # Note: OpenRouter, Together, Cerebras not directly supported by Helicone
        # Would need custom provider configuration
    }
    return models

def update_gateway_config():
    """Update the gateway configuration with discovered models"""
    
    available_models = get_available_models()
    
    # Combine models prioritizing free/fast options
    all_models = (
        available_models["groq"][:3] +      # Top 3 Groq models
        available_models["gemini"][:2] +    # Top 2 Gemini models  
        available_models["mistral"][:1]     # Top 1 Mistral model
    )
    
    fast_models = (
        available_models["groq"][:2] +      # Top 2 Groq (fastest)
        available_models["gemini"][:1]      # Top 1 Gemini
    )
    
    # Create new configuration
    config = {
        "telemetry": {
            "level": "info,ai_gateway=debug",
            "exporter": "both"
        },
        "routers": {
            "main": {
                "load-balance": {
                    "chat": {
                        "strategy": "model-latency",
                        "models": all_models
                    }
                }
            },
            "fast": {
                "load-balance": {
                    "chat": {
                        "strategy": "model-latency", 
                        "models": fast_models
                    }
                }
            }
        }
    }
    
    # Write updated config
    config_path = "/Users/antonioreid/CODE/00_PROJECTS/00_APPS/00_AI_GATEWAY_v2/ai-gateway/config.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    # Log the update
    print(f"✅ Updated config with {len(all_models)} models:")
    for model in all_models:
        print(f"  - {model}")
    
    return config

if __name__ == "__main__":
    print(f"🔍 Discovering models at {datetime.now()}")
    update_gateway_config()
    print("🎯 Configuration updated successfully!")
