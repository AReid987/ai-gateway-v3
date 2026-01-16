# Migration Guide: Root to Turborepo Structure

This guide explains the changes made to restructure the project to follow Turborepo conventions.

## What Changed?

### Before (Root-level code)
```
ai-gateway-v2/
├── ai-gateway/              # Helicone gateway
├── gateway_client.py        # Reusable client (root level)
├── claude_flow_hive.py      # Claude Flow code (root level)
├── claude_flow_swarm.py     # Claude Flow code (root level)
├── test_*.py                # Test files (root level)
└── package.json
```

### After (Turborepo structure)
```
ai-gateway-v3/
├── apps/                    # Standalone applications
│   └── (future: ai-gateway/)
├── packages/                # Reusable packages
│   ├── gateway-client/      # ✨ NEW: Reusable Python client
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   └── gateway_client.py
│   │   ├── setup.py
│   │   └── README.md
│   └── claude-flow/         # ✨ NEW: Claude Flow integration
│       ├── src/
│       │   ├── __init__.py
│       │   ├── integration.py
│       │   ├── hive.py
│       │   └── swarm.py
│       ├── setup.py
│       └── README.md
├── ai-gateway/              # (to be moved to apps/)
└── package.json             # Updated with workspace config
```

## Migration Steps

### 1. Update Your Imports

**Old way (root-level imports):**
```python
from gateway_client import GatewayFactory
from claude_flow_hive import Hive, Agent
from claude_flow_swarm import Swarm
```

**New way (package imports):**
```python
# After installing packages
from gateway_client import GatewayFactory
from claude_flow import Hive, Agent, Swarm
```

### 2. Install the Packages

This project uses **PDM with uv** for Python package management.

```bash
# Using pdm (recommended)
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow

# Or using uv directly
uv pip install -e packages/gateway-client
uv pip install -e packages/claude-flow
```

### 3. Update Your Scripts

**Old:**
```bash
python test_gateway.py
python test_claude_flow.py
```

**New:**
```bash
# Tests are now in package directories
python -m pytest packages/gateway-client/tests
python -m pytest packages/claude-flow/tests
```

### 4. Use Turborepo Commands

```bash
# Build all packages
pnpm run build

# Run development mode
pnpm run dev

# Run linting
pnpm run lint
```

## Benefits of the New Structure

1. **Reusability**: Packages can be imported in any Python project
2. **Isolation**: Each package has its own dependencies and tests
3. **Scalability**: Easy to add new packages or apps
4. **Standards**: Follows Turborepo and Python packaging best practices
5. **Versioning**: Each package can be versioned independently

## Backward Compatibility

The old root-level files are still present for backward compatibility:
- `gateway_client.py`
- `claude_flow_hive.py`
- `claude_flow_swarm.py`
- `test_*.py`

These will be deprecated in a future release. Please migrate to the package imports.

## Next Steps

1. ✅ Packages created and structured
2. ⏳ Move `ai-gateway/` to `apps/ai-gateway/`
3. ⏳ Create example applications in `apps/examples/`
4. ⏳ Add comprehensive tests to each package
5. ⏳ Set up CI/CD with Turborepo

## Need Help?

- Check package READMEs: `packages/*/README.md`
- Review examples in the main README.md
- See `REUSABLE_PATTERNS.md` for common patterns

