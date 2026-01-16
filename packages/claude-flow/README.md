# Claude Flow AI Gateway Integration

Claude Flow integration that uses the AI Gateway instead of LiteLLM.

## Features

- **LiteLLM Compatible**: Drop-in replacement for LiteLLM in Claude Flow
- **Multiple Providers**: Access to Groq, Gemini, Mistral, and more
- **Automatic Fallbacks**: Switches providers when one fails
- **Hive & Swarm Patterns**: Multi-agent collaboration patterns

## Installation

This project uses **uv** with virtual environments for Python package management.

```bash
# From project root, create and activate venv
uv venv
source .venv/bin/activate

# Install this package
uv pip install -e ./packages/claude-flow

# Or using traditional pip (in activated venv)
pip install -e ./packages/claude-flow

# Or using npm script (in activated venv)
pnpm run install:packages
```

> **Important**: Always activate the virtual environment first!

## Usage

### Basic Completion

```python
from claude_flow import claude_flow_completion

result = claude_flow_completion(
    "Analyze this code for potential issues",
    model="claude-3-haiku"
)
```

### Hive Pattern (Multi-Agent Collaboration)

```python
from claude_flow import Hive

hive = Hive("research-team")
hive.add_agent("researcher", "a thorough researcher")
hive.add_agent("analyst", "a critical analyst")
hive.add_agent("writer", "a clear technical writer")

results = await hive.collaborate("Research AI safety best practices")
```

### Swarm Pattern (Coordinated Hives)

```python
from claude_flow import Swarm, Hive

swarm = Swarm("project-team")

# Add specialized hives
research_hive = Hive("research")
dev_hive = Hive("development")

swarm.add_hive(research_hive)
swarm.add_hive(dev_hive)

result = await swarm.execute("Build a secure authentication system")
```

