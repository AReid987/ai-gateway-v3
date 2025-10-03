#!/usr/bin/env python3
"""
Claude Flow Workflow Example using AI Gateway
Demonstrates how to use our AI Gateway in Claude Flow workflows
"""

import json
from claude_flow_integration import claude_flow_completion, claude_flow_chat

class AIGatewayWorkflow:
    """Claude Flow workflow using AI Gateway"""
    
    def __init__(self, config_path: str = "claude-flow-config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
    
    def analyze_code(self, code: str) -> str:
        """Analyze code using AI Gateway"""
        prompt = f"""
        Analyze this code and provide:
        1. Brief summary
        2. Potential issues
        3. Suggestions for improvement
        
        Code:
        ```
        {code}
        ```
        """
        
        return claude_flow_completion(prompt, model="claude-3-haiku")
    
    def generate_documentation(self, code: str) -> str:
        """Generate documentation using AI Gateway"""
        prompt = f"""
        Generate clear documentation for this code:
        
        ```
        {code}
        ```
        
        Include:
        - Purpose and functionality
        - Parameters and return values
        - Usage examples
        """
        
        return claude_flow_completion(prompt, model="claude-3-sonnet")
    
    def chat_workflow(self, user_input: str, context: list = None) -> str:
        """Interactive chat workflow"""
        messages = context or []
        messages.append({"role": "user", "content": user_input})
        
        return claude_flow_chat(messages, model="claude-3-haiku")

# Example workflow execution
def run_example_workflow():
    """Run example Claude Flow workflow with AI Gateway"""
    
    workflow = AIGatewayWorkflow()
    
    # Example code to analyze
    sample_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    '''
    
    print("🔍 Analyzing code...")
    analysis = workflow.analyze_code(sample_code)
    print(f"Analysis: {analysis}\n")
    
    print("📝 Generating documentation...")
    docs = workflow.generate_documentation(sample_code)
    print(f"Documentation: {docs}\n")
    
    print("💬 Chat workflow...")
    response = workflow.chat_workflow("How can I optimize the fibonacci function?")
    print(f"Chat response: {response}")

if __name__ == "__main__":
    run_example_workflow()
