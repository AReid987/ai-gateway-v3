# AI Gateway v3 - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (1 min)

```bash
# Install Node.js dependencies
pnpm install

# Install Python packages (using PDM with uv)
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow

# Or using uv directly
uv pip install -e packages/gateway-client
uv pip install -e packages/claude-flow
```

### Step 2: Build the Gateway (2 min)

```bash
cd ai-gateway
cargo build --release
cd ..
```

### Step 3: Set Up API Keys (1 min)

Create or edit `~/.zsh_secrets`:

```bash
# Required for testing
export GROQ_API_KEY="gsk_..."           # Get from https://console.groq.com
export GEMINI_API_KEY="AIza..."         # Get from https://aistudio.google.com

# Optional (for more providers)
export MISTRAL_API_KEY="..."            # Get from https://console.mistral.ai
export ANTHROPIC_API_KEY="sk-ant-..."   # Get from https://console.anthropic.com
export OPENAI_API_KEY="sk-..."          # Get from https://platform.openai.com
```

Then load them:
```bash
source ~/.zsh_secrets
```

### Step 4: Start the Gateway (30 sec)

```bash
cd ai-gateway
./target/release/ai-gateway --config config.yaml
```

You should see:
```
🚀 AI Gateway v3 starting...
✅ Server listening on http://0.0.0.0:8080
```

### Step 5: Test It! (30 sec)

In a new terminal:

```bash
# Simple health check
curl http://localhost:8080/health

# Run the test script
python test_gateway_simple.py
```

## 🎯 What You Can Do Now

### 1. Use the Gateway Client

```python
from gateway_client import GatewayFactory

# Create a client
client = GatewayFactory.balanced()

# Make a request
response = client.chat_completion(
    model="groq/llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=100
)

print(response['choices'][0]['message']['content'])
```

### 2. Try Claude Flow Hive Pattern

```python
from claude_flow import Hive
import asyncio

async def run_hive():
    # Create a hive of agents
    hive = Hive("research-team")
    hive.add_agent("researcher", "a thorough researcher")
    hive.add_agent("analyst", "a critical analyst")
    hive.add_agent("writer", "a clear technical writer")
    
    # Collaborate on a task
    results = await hive.collaborate("Research AI safety best practices")
    
    for agent_name, result in results.items():
        print(f"\n{agent_name}:")
        print(result)

# Run it
asyncio.run(run_hive())
```

### 3. Try Claude Flow Swarm Pattern

```python
from claude_flow import Swarm, Hive
import asyncio

async def run_swarm():
    # Create a swarm
    swarm = Swarm("AI Project Team")
    
    # Add research hive
    research_hive = Hive("Research")
    research_hive.add_agent("researcher", "a thorough researcher")
    research_hive.add_agent("analyst", "a data analyst")
    swarm.add_hive(research_hive)
    
    # Add development hive
    dev_hive = Hive("Development")
    dev_hive.add_agent("architect", "a software architect")
    dev_hive.add_agent("developer", "a senior developer")
    swarm.add_hive(dev_hive)
    
    # Execute a mission
    results = await swarm.execute_mission("Build a secure authentication system")
    
    print(results)

# Run it
asyncio.run(run_swarm())
```

## 🔧 Troubleshooting

### Gateway won't start?

1. **Check if port 8080 is in use:**
   ```bash
   lsof -i :8080
   ```

2. **Rebuild the gateway:**
   ```bash
   cd ai-gateway
   cargo clean
   cargo build --release
   ```

3. **Check API keys are loaded:**
   ```bash
   echo $GROQ_API_KEY
   ```

### Requests failing?

1. **Check gateway is running:**
   ```bash
   curl http://localhost:8080/health
   ```

2. **Check gateway logs:**
   ```bash
   tail -f ai-gateway/gateway.log
   ```

3. **Try a different model:**
   - `groq/llama-3.1-8b-instant` (usually has free quota)
   - `gemini/gemini-2.0-flash` (Google's free tier)

### Import errors?

Make sure packages are installed:
```bash
# Using pdm (recommended)
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow

# Or using uv
uv pip install -e packages/gateway-client
uv pip install -e packages/claude-flow
```

## 📚 Next Steps

1. **Read the docs:**
   - [README.md](README.md) - Full documentation
   - [START_GATEWAY.md](START_GATEWAY.md) - Detailed gateway instructions
   - [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Migration from old structure
   - [PROJECT_STATUS.md](PROJECT_STATUS.md) - Current project status

2. **Explore the packages:**
   - `packages/gateway-client/README.md` - Gateway client documentation
   - `packages/claude-flow/README.md` - Claude Flow documentation

3. **Check out examples:**
   - `test_gateway_simple.py` - Simple gateway test
   - `REUSABLE_PATTERNS.md` - Common patterns

## 🎉 You're Ready!

You now have:
- ✅ A running AI Gateway with intelligent routing
- ✅ Access to multiple free AI providers (Groq, Gemini, Mistral)
- ✅ Reusable Python packages for easy integration
- ✅ Multi-agent collaboration patterns (Hive & Swarm)

Start building! 🚀

