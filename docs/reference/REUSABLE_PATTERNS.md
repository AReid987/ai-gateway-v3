# Reusable AI Gateway Patterns

## Gateway Client Pattern

```python
from gateway_client import GatewayFactory

# For balanced routing across all providers
client = GatewayFactory.balanced()

# For speed-optimized routing (Groq priority)
client = GatewayFactory.fast()

# Custom routing
client = AIGatewayClient(router_id="custom")
```

## Agent Pattern

```python
from claude_flow_hive import Agent
from gateway_client import GatewayFactory

agent = Agent(
    name="specialist",
    role="domain expert in X",
    model="groq/llama-3.1-70b-versatile",
    gateway=GatewayFactory.balanced()
)

result = await agent.process("task description")
```

## Hive Pattern (Team Collaboration)

```python
from claude_flow_hive import Hive

hive = Hive("Team Name")
hive.add_agent("role1", "description", "model1")
hive.add_agent("role2", "description", "model2")

results = await hive.collaborate("shared task")
```

## Swarm Pattern (Multi-Team Coordination)

```python
from claude_flow_swarm import Swarm

swarm = Swarm("Project Name")
swarm.add_hive(hive1)
swarm.add_hive(hive2)

results = await swarm.execute_mission("complex mission")
```

## Reusability for Other Projects

### 1. Copy Core Files

- `gateway_client.py` - Gateway abstraction
- `claude_flow_hive.py` - Agent/Hive classes
- `claude_flow_swarm.py` - Swarm coordination

### 2. Customize for Your Domain

```python
# Custom agent roles
def create_marketing_hive():
    hive = Hive("Marketing Team")
    hive.add_agent("copywriter", "creative copywriter")
    hive.add_agent("strategist", "marketing strategist")
    return hive

# Custom swarm missions
async def marketing_campaign(brief):
    swarm = Swarm("Campaign Swarm")
    swarm.add_hive(create_marketing_hive())
    return await swarm.execute_mission(f"Create campaign: {brief}")
```

### 3. Model Selection Strategy

- **Fast tasks**: `groq/llama-3.3-70b-versatile`
- **Complex reasoning**: `google/gemini-2.5-pro`
- **Creative tasks**: `gemini/gemini-2.0-flash`
- **Code tasks**: `zai/glm-4.6`

### 4. Gateway Benefits

- **Free quota optimization**: Rotates across providers
- **Automatic fallbacks**: Handles provider failures
- **Dynamic models**: Updates daily with new free models
- **Load balancing**: Distributes requests efficiently
