#!/usr/bin/env python3
"""
Claude Flow AI Gateway Integration
Replaces LiteLLM with our AI Gateway for Claude Flow workflows
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional

class AIGatewayClient:
    """Client for our AI Gateway that mimics LiteLLM interface"""
    
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        stream: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        LiteLLM-compatible completion method using our AI Gateway
        """
        
        # Map model names to our gateway format
        model_mapping = {
            "claude-3-sonnet": "anthropic/claude-3-5-sonnet",
            "claude-3-haiku": "anthropic/claude-3-5-haiku", 
            "gpt-4": "openai/gpt-4o-mini",
            "gpt-3.5-turbo": "openai/gpt-4o-mini",
            "llama-2": "groq/llama-3.1-8b-instant",
            "gemini-pro": "gemini/gemini-2.0-flash"
        }
        
        gateway_model = model_mapping.get(model, f"groq/{model}")
        
        payload = {
            "model": gateway_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
            **kwargs
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/ai/chat/completions",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                # Fallback to different model on error
                fallback_models = [
                    "groq/llama-3.1-8b-instant",
                    "gemini/gemini-2.0-flash", 
                    "mistral/mistral-small"
                ]
                
                for fallback in fallback_models:
                    if fallback != gateway_model:
                        payload["model"] = fallback
                        fallback_response = self.session.post(
                            f"{self.base_url}/ai/chat/completions",
                            json=payload,
                            headers={"Content-Type": "application/json"},
                            timeout=30
                        )
                        if fallback_response.status_code == 200:
                            return fallback_response.json()
                
                # If all fail, return error
                return {
                    "error": {
                        "message": f"All models failed. Last error: {response.text}",
                        "type": "gateway_error"
                    }
                }
                
        except Exception as e:
            return {
                "error": {
                    "message": f"Gateway request failed: {str(e)}",
                    "type": "connection_error"
                }
            }

# Global client instance
gateway_client = AIGatewayClient()

def claude_flow_completion(prompt: str, model: str = "claude-3-haiku") -> str:
    """
    Claude Flow compatible completion function
    """
    messages = [{"role": "user", "content": prompt}]
    
    response = gateway_client.completion(
        model=model,
        messages=messages,
        max_tokens=2000,
        temperature=0.7
    )
    
    if "error" in response:
        raise Exception(f"AI Gateway Error: {response['error']['message']}")
    
    return response["choices"][0]["message"]["content"]

def claude_flow_chat(messages: List[Dict[str, str]], model: str = "claude-3-haiku") -> str:
    """
    Claude Flow compatible chat function
    """
    response = gateway_client.completion(
        model=model,
        messages=messages,
        max_tokens=2000,
        temperature=0.7
    )
    
    if "error" in response:
        raise Exception(f"AI Gateway Error: {response['error']['message']}")
    
    return response["choices"][0]["message"]["content"]

# Example usage for Claude Flow workflows
if __name__ == "__main__":
    # Test the integration
    try:
        result = claude_flow_completion(
            "Hello! Please respond with 'AI Gateway integration working!'",
            model="claude-3-haiku"
        )
        print(f"✅ Success: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
