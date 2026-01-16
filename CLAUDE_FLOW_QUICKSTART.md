# Claude Flow Quick Start Guide

## Prerequisites

1. **Virtual environment activated**
2. **Gateway running**
3. **API keys loaded**

## Step 1: Activate Virtual Environment

```bash
cd /Users/antonioreid/CODE/00_PROJECTS/00_APPS/00_AI_GATEWAY_v2
source .venv/bin/activate
```

## Step 2: Start the Gateway

In **Terminal 1**:

```bash
cd apps/ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml
```

You should see:
```
🚀 AI Gateway started on http://localhost:8080
```

## Step 3: Use Claude Flow

In **Terminal 2** (new terminal):

```bash
cd /Users/antonioreid/CODE/00_PROJECTS/00_APPS/00_AI_GATEWAY_v2
source .venv/bin/activate
```

### Option A: Simple Hive Example

Create a file `test_hive.py`:

```python
from hive import Hive, Agent
from gateway_client import GatewayFactory

# Create gateway client
gateway = GatewayFactory.balanced()

# Create agents
researcher = Agent(
    name="Researcher",
    role="Research and gather information",
    gateway_client=gateway
)

writer = Agent(
    name="Writer", 
    role="Write clear and concise content",
    gateway_client=gateway
)

# Create hive
hive = Hive(
    name="Content Creation Hive",
    agents=[researcher, writer],
    gateway_client=gateway
)

# Run task
result = hive.run("Write a short article about AI gateways")
print(result)
```

Run it:
```bash
python test_hive.py
```

### Option B: Swarm Example

Create a file `test_swarm.py`:

```python
from swarm import Swarm
from hive import Hive, Agent
from gateway_client import GatewayFactory

# Create gateway client
gateway = GatewayFactory.balanced()

# Create research hive
research_hive = Hive(
    name="Research Team",
    agents=[
        Agent("Researcher 1", "Technical research", gateway),
        Agent("Researcher 2", "Market research", gateway)
    ],
    gateway_client=gateway
)

# Create writing hive
writing_hive = Hive(
    name="Writing Team",
    agents=[
        Agent("Writer", "Content creation", gateway),
        Agent("Editor", "Content editing", gateway)
    ],
    gateway_client=gateway
)

# Create swarm
swarm = Swarm(
    name="Content Production Swarm",
    hives=[research_hive, writing_hive],
    gateway_client=gateway
)

# Run coordinated task
result = swarm.run("Create a comprehensive guide about AI routing")
print(result)
```

Run it:
```bash
python test_swarm.py
```

### Option C: Direct Gateway Client

Create a file `test_direct.py`:

```python
from gateway_client import AIGatewayClient

# Create client
client = AIGatewayClient(base_url="http://localhost:8080")

# Send request
response = client.chat_completion(
    model="llama-3.3-70b-versatile",  # Groq model
    messages=[
        {"role": "user", "content": "Hello! Tell me about AI gateways."}
    ]
)

print(response['choices'][0]['message']['content'])
```

Run it:
```bash
python test_direct.py
```

## Step 4: Verify Gateway is Working

Quick health check:

```bash
curl http://localhost:8080/health
```

Should return:
```json
{"status":"ok"}
```

## Available Models

The gateway routes to these providers (with your API keys):

### Groq (Fast, Free Tier)
- `llama-3.3-70b-versatile`
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`

### Google Gemini
- `gemini-1.5-flash`
- `gemini-1.5-pro`

### Others (if configured)
- Mistral
- Anthropic Claude
- OpenAI

## Common Patterns

### 1. Simple Agent

```python
from hive import Agent
from gateway_client import GatewayFactory

agent = Agent(
    name="Assistant",
    role="Helpful AI assistant",
    gateway_client=GatewayFactory.balanced()
)

response = agent.execute("What is 2+2?")
print(response)
```

### 2. Multi-Agent Collaboration

```python
from hive import Hive, Agent
from gateway_client import GatewayFactory

gateway = GatewayFactory.balanced()

hive = Hive(
    name="Problem Solvers",
    agents=[
        Agent("Analyst", "Analyze problems", gateway),
        Agent("Solver", "Propose solutions", gateway),
        Agent("Critic", "Evaluate solutions", gateway)
    ],
    gateway_client=gateway
)

result = hive.run("How can we improve code quality?")
print(result)
```

### 3. Using Specific Router

```python
from gateway_client import AIGatewayClient

# Use fast router for quick responses
fast_client = AIGatewayClient(
    base_url="http://localhost:8080",
    router_id="fast"
)

response = fast_client.chat_completion(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Quick question: What is AI?"}]
)
```

## Troubleshooting

### Error: "Connection refused"

**Problem**: Gateway not running

**Solution**:
```bash
cd apps/ai-gateway
./target/release/ai-gateway --config config.yaml
```

### Error: "ModuleNotFoundError: No module named 'hive'"

**Problem**: Virtual environment not activated or packages not installed

**Solution**:
```bash
source .venv/bin/activate
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow
```

### Error: "API key not found"

**Problem**: API keys not loaded

**Solution**:
```bash
source ~/.zsh_secrets
echo $GROQ_API_KEY  # Should show your key
```

### Error: "No route found"

**Problem**: Model not configured in gateway config

**Solution**: Check `apps/ai-gateway/config.yaml` for available models

## Testing

Run the integration tests:

```bash
# Make sure gateway is running first!
python test_claude_flow_integration.py
```

## Configuration

### Gateway Config

Edit `apps/ai-gateway/config.yaml` to configure:
- Available models
- Routing strategies
- Load balancing
- Fallback behavior

### Custom Gateway URL

```python
from gateway_client import AIGatewayClient

client = AIGatewayClient(base_url="http://your-gateway:8080")
```

## Next Steps

1. **Explore Examples**: Check `apps/examples/` for more examples
2. **Read Docs**: See `docs/reference/CLAUDE_FLOW_INTEGRATION.md`
3. **Customize**: Modify agents and hives for your use case
4. **Scale**: Deploy gateway for production use

## Quick Reference

```bash
# Start gateway
cd apps/ai-gateway && ./target/release/ai-gateway --config config.yaml

# Activate venv
source .venv/bin/activate

# Test gateway
curl http://localhost:8080/health

# Run Python script
python your_script.py
```

## Example: Complete Workflow

```python
#!/usr/bin/env python3
"""
Complete Claude Flow example with the AI Gateway
"""

from hive import Hive, Agent
from gateway_client import GatewayFactory

def main():
    # Create gateway client
    print("🔌 Connecting to AI Gateway...")
    gateway = GatewayFactory.balanced()
    
    # Create agents
    print("🤖 Creating agents...")
    agents = [
        Agent("Planner", "Plan and organize tasks", gateway),
        Agent("Executor", "Execute planned tasks", gateway),
        Agent("Reviewer", "Review and validate results", gateway)
    ]
    
    # Create hive
    print("🐝 Creating hive...")
    hive = Hive(
        name="Task Management Hive",
        agents=agents,
        gateway_client=gateway
    )
    
    # Run task
    print("🚀 Running task...")
    task = "Create a plan to organize a team meeting"
    result = hive.run(task)
    
    print("\n✅ Result:")
    print(result)

if __name__ == "__main__":
    main()
```

Save as `complete_example.py` and run:
```bash
python complete_example.py
```

---

**Need help?** See [QUICK_REFERENCE.md](QUICK_REFERENCE.md) or [INSTALLATION.md](INSTALLATION.md)

