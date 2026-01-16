# AI Gateway Client

Reusable Python client for the AI Gateway.

## Installation

This project uses **uv** with virtual environments for Python package management.

```bash
# From project root, create and activate venv
uv venv
source .venv/bin/activate

# Install this package
uv pip install -e ./packages/gateway-client

# Or using traditional pip (in activated venv)
pip install -e ./packages/gateway-client

# Or using npm script (in activated venv)
pnpm run install:packages
```

> **Important**: Always activate the virtual environment first!

## Usage

```python
from gateway_client import GatewayFactory

# For balanced routing across all providers
client = GatewayFactory.balanced()

# For speed-optimized routing (Groq priority)
client = GatewayFactory.fast()

# Make a request
response = client.chat_completion(
    model="groq/llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=100
)
```

## Features

- Multiple routing strategies (balanced, fast, custom)
- Automatic retries and fallbacks
- Support for all AI Gateway endpoints
- Type hints for better IDE support

