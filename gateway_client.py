"""
Reusable AI Gateway Client for Claude Flow and other projects
"""
import requests
import json
from typing import Dict, List, Optional, Any

class AIGatewayClient:
    def __init__(self, base_url: str = "http://localhost:8080", router_id: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.router_id = router_id
        
    def chat_completion(self, model: str, messages: List[Dict], **kwargs) -> Dict[str, Any]:
        """Send chat completion request through AI Gateway"""
        headers = {"Content-Type": "application/json"}
        if self.router_id:
            headers["X-Router-Id"] = self.router_id
            
        payload = {
            "model": model,
            "messages": messages,
            **kwargs
        }
        
        response = requests.post(
            f"{self.base_url}/ai/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def get_available_models(self) -> List[str]:
        """Get list of available models from gateway"""
        response = requests.get(f"{self.base_url}/health")
        # Parse from gateway config or implement models endpoint
        return ["groq/llama-3.1-8b-instant", "gemini/gemini-2.0-flash", "mistral/mistral-small"]

# Factory for different routing strategies
class GatewayFactory:
    @staticmethod
    def balanced() -> AIGatewayClient:
        return AIGatewayClient()
    
    @staticmethod
    def fast() -> AIGatewayClient:
        return AIGatewayClient(router_id="fast")
