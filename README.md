# AI Gateway v3 - Turborepo Monorepo

A high-performance AI Gateway built on Helicone's open-source AI Gateway with **dynamic model discovery** that automatically updates available free models daily.

## 📁 Project Structure (Turborepo)

This project follows Turborepo conventions for better organization and reusability:

```
ai-gateway-v3/
├── apps/                    # Standalone applications
│   ├── ai-gateway/          # Helicone AI Gateway (Rust)
│   ├── docs/                # Documentation site
│   └── examples/            # Example scripts
├── packages/                # Reusable packages
│   ├── gateway-client/      # Python client for AI Gateway
│   └── claude-flow/         # Claude Flow integration
├── docs/                    # Documentation
│   ├── development/         # Development logs
│   ├── guides/              # User guides (Quick Start, Testing, etc.)
│   └── reference/           # Reference docs (Claude, Gemini, etc.)
├── scripts/                 # Utility scripts
│   ├── discover_models.py   # Model discovery script
│   └── setup_daily_discovery.sh
├── package.json            # Root package configuration
├── pyproject.toml          # PDM configuration
├── turbo.json              # Turborepo configuration
└── pnpm-workspace.yaml     # PNPM workspace configuration
```

## 🚀 Key Features

- **Dynamic Model Discovery**: Automatically discovers free models from providers daily
- **Intelligent Routing**: Routes requests to the best available model based on latency and health
- **Load Balancing**: Distributes requests across multiple providers to maximize quota utilization
- **Automatic Fallbacks**: Seamlessly switches to alternative providers when primary ones fail
- **Free Tier Optimization**: Focuses on providers with free quotas (Groq, Gemini, Mistral, etc.)

## 🎯 Supported Providers (Free Tier Focus)

<!-- TODO: Update Models Table to fix any innaccuracies -->

| Provider          | Models                                                        | Auto-Discovery |
| ----------------- | ------------------------------------------------------------- | -------------- |
| **Groq**          | `llama-3.1-8b-instant`, `llama-3.1-70b-versatile`             | ✅              |
| **Google Gemini** | `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-lite` | ✅              |
| **Mistral**       | `mistral-small`, `codestral-mamba`                            | ✅              |
| **OpenRouter**    | Free models (changes daily)                                   | 🔄 Planned      |
| **Together AI**   | Free tier models                                              | 🔄 Planned      |
| **Cerebras**      | `llama3.1-8b`, `llama3.1-70b`                                 | 🔄 Planned      |

## 🔄 Dynamic Model Discovery

The gateway automatically discovers and updates available models:

### Daily Auto-Discovery

```bash
# Runs automatically at 6:00 AM daily via cron
# Discovers free models from all providers
# Updates gateway configuration automatically
```

### Manual Discovery

```bash
# Run model discovery manually
python3 scripts/discover_models.py

# Setup daily cron job
./scripts/setup_daily_discovery.sh
```

## 🚦 Quick Start

### 1. Install Dependencies

```bash
# Install Node.js dependencies
pnpm install

# Create Python virtual environment
uv venv
source .venv/bin/activate  # On macOS/Linux
# Or on Windows: .venv\Scripts\activate

# Install Python packages (in activated venv)
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# Or using npm script (in activated venv)
pnpm run install:packages
```

> **Important**: Always activate the virtual environment before installing packages or running Python code!
> See [INSTALLATION.md](INSTALLATION.md) for detailed instructions or [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for quick commands.

### 2. Setup & Start Gateway

```bash
# Build the gateway
pnpm run gateway:build

# Setup daily model discovery
./scripts/setup_daily_discovery.sh

# Start the gateway
cd apps/ai-gateway
source ~/.zsh_secrets  # Load your API keys
./target/release/ai-gateway --config config.yaml

# Or use the npm script
pnpm run gateway:start
```

### 3. Test the Gateway

```bash
# Health check
curl http://localhost:8080/health

# Test with Groq (usually has free quota)
curl -X POST http://localhost:8080/ai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "groq/llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 50
  }'

# Test with Gemini
curl -X POST http://localhost:8080/ai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.0-flash",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 50
  }'
```

## 📦 Using the Reusable Packages

### Gateway Client Package (`@ai-gateway/client`)

```python
from gateway_client import GatewayFactory

# Create a client with balanced routing
client = GatewayFactory.balanced()

# Make a request
response = client.chat_completion(
    model="groq/llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=100
)
print(response['choices'][0]['message']['content'])
```

### Claude Flow Package (`@ai-gateway/claude-flow`)

```python
from claude_flow import Hive, claude_flow_completion
import asyncio

# Simple completion
result = claude_flow_completion(
    "Explain quantum computing in simple terms",
    model="claude-3-haiku"
)

# Multi-agent collaboration
async def run_hive():
    hive = Hive("research-team")
    hive.add_agent("researcher", "a thorough researcher")
    hive.add_agent("analyst", "a critical analyst")
    hive.add_agent("writer", "a clear technical writer")

    results = await hive.collaborate("Research AI safety best practices")
    return results

# Run the hive
results = asyncio.run(run_hive())
```

## 🎛️ Router Configuration

### Main Router (Balanced)

- **Strategy**: Model latency-based routing
- **Models**: Auto-discovered from all providers
- **Use case**: Balanced performance and quota distribution

### Fast Router (Speed-Optimized)

- **Strategy**: Latency-optimized routing
- **Models**: Fastest models (Groq priority)
- **Use case**: Speed-critical applications

## 📡 API Usage

### Basic Request (Auto-Routing)

```bash
curl -X POST http://localhost:8080/ai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "groq/llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Using Fast Router

```bash
curl -X POST http://localhost:8080/ai/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-Router-Id: fast" \
  -d '{
    "model": "groq/llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## 🔧 Configuration

### Environment Variables

Set your API keys in `~/.zsh_secrets`:

```bash
# Required for supported providers
export GROQ_API_KEY="gsk_..."
export GEMINI_API_KEY="AIza..."
export MISTRAL_API_KEY="..."

# Optional for future providers
export OPENROUTER_API_KEY="sk-or-v1-..."
export TOGETHER_API_KEY="..."
export CEREBRAS_API_KEY="csk_..."
```

### Model Discovery Configuration

Edit `scripts/discover_models.py` to customize:

```python
# Add new providers
PROVIDERS = {
    "new_provider": {
        "url": "https://api.newprovider.com/models",
        "headers": {"Authorization": f"Bearer {os.getenv('NEW_PROVIDER_KEY')}"},
        "free_filter": lambda m: m.get('free', False)
    }
}
```

## 📊 Benefits

1. **Always Up-to-Date**: Models are discovered daily, ensuring access to latest free offerings
2. **Quota Maximization**: Distributes requests across all available free providers
3. **Zero Maintenance**: Automatic discovery means no manual model list updates
4. **Cost Optimization**: Focuses on free tier models to minimize costs
5. **High Availability**: Automatic fallbacks ensure requests succeed

## 🔄 How Dynamic Discovery Works

1. **Daily Scan**: Cron job runs at 6:00 AM daily
2. **Provider Query**: Checks each provider's API for available models
3. **Free Filter**: Identifies models with free quotas or pricing
4. **Config Update**: Updates `config.yaml` with discovered models
5. **Gateway Reload**: Configuration is automatically applied

## 🚨 Troubleshooting

### Model Discovery Issues

```bash
# Check discovery logs
tail -f logs/model_discovery.log

# Run discovery manually
python3 scripts/discover_models.py

# Check cron job status
crontab -l | grep discover_models
```

### API Key Issues

- Verify keys are set in `~/.zsh_secrets`
- Check provider-specific key formats
- Ensure keys have sufficient quota

### Gateway Issues

- Check that port 8080 is available
- Verify configuration: `./target/release/ai-gateway --config config.yaml --validate`
- Check logs: `tail -f ai-gateway/gateway.log`

## 🎯 Future Enhancements

- [ ] OpenRouter free model discovery
- [ ] Together AI integration
- [ ] Cerebras model support
- [ ] Real-time quota monitoring
- [ ] Model performance analytics
- [ ] Custom provider plugins

---

**Built with ❤️ using Helicone AI Gateway + Dynamic Discovery**
