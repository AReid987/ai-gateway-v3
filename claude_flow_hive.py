"""
Claude Flow Hive using AI Gateway v2
"""
from gateway_client import AIGatewayClient, GatewayFactory
from typing import List, Dict, Any, Optional
import asyncio
import json

class Agent:
    def __init__(self, name: str, role: str, model: str, gateway: AIGatewayClient):
        self.name = name
        self.role = role
        self.model = model
        self.gateway = gateway
        
    async def process(self, task: str, context: Optional[str] = None) -> str:
        """Process a task using the AI Gateway"""
        messages = [
            {"role": "system", "content": f"You are {self.role}. {context or ''}"},
            {"role": "user", "content": task}
        ]
        
        response = self.gateway.chat_completion(
            model=self.model,
            messages=messages,
            max_tokens=500
        )
        
        return response['choices'][0]['message']['content']

class Hive:
    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []
        self.gateway = GatewayFactory.balanced()
        
    def add_agent(self, name: str, role: str, model: str = "groq/llama-3.1-8b-instant"):
        """Add agent to hive"""
        agent = Agent(name, role, model, self.gateway)
        self.agents.append(agent)
        return agent
        
    async def collaborate(self, task: str) -> Dict[str, str]:
        """Have all agents collaborate on a task"""
        results = {}
        for agent in self.agents:
            result = await agent.process(task)
            results[agent.name] = result
        return results

# Example hive setup
def create_research_hive() -> Hive:
    hive = Hive("Research Team")
    hive.add_agent("researcher", "a thorough researcher", "groq/llama-3.1-70b-versatile")
    hive.add_agent("analyst", "a data analyst", "gemini/gemini-2.0-flash")
    hive.add_agent("writer", "a technical writer", "mistral/mistral-small")
    return hive
