# AI Gateway v3 - Quick Reference

## Installation (One-Time Setup)

```bash
# 1. Clone repository
git clone git@github.com:AReid987/ai-gateway-v3.git
cd ai-gateway-v3

# 2. Install Node.js dependencies
pnpm install

# 3. Create Python virtual environment
uv venv
source .venv/bin/activate

# 4. Install Python packages
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# 5. Build gateway
pnpm run gateway:build

# 6. Setup API keys (edit ~/.zsh_secrets)
source ~/.zsh_secrets
```

## Daily Workflow

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Start gateway
cd apps/ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml

# 3. In another terminal, run tests
source .venv/bin/activate
python test_packages_structure.py
python test_gateway_simple.py
```

## Common Commands

### Virtual Environment

```bash
# Create venv
uv venv

# Activate venv (macOS/Linux)
source .venv/bin/activate

# Activate venv (Windows)
.venv\Scripts\activate

# Deactivate venv
deactivate
```

### Package Installation

```bash
# Install with uv (in activated venv)
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# Or with pip (in activated venv)
pip install -e ./packages/gateway-client
pip install -e ./packages/claude-flow

# Or using npm script (in activated venv)
pnpm run install:packages
```

### Gateway

```bash
# Build gateway
pnpm run gateway:build
# Or manually:
cd apps/ai-gateway && cargo build --release

# Start gateway
pnpm run gateway:start
# Or manually:
cd apps/ai-gateway
./target/release/ai-gateway --config config.yaml

# Check if gateway is running
curl http://localhost:8080/health
```

### Testing

```bash
# Test package structure (no gateway needed)
python test_packages_structure.py

# Test gateway (requires running gateway)
python test_gateway_simple.py

# Full integration tests (requires running gateway)
python test_claude_flow_integration.py
```

### PDM Scripts

```bash
# Build gateway
pdm run gateway-build

# Start gateway
pdm run gateway-start

# Run tests
pdm run test-structure
pdm run test-gateway
pdm run test-integration
```

## File Locations

### Gateway
- **Binary**: `apps/ai-gateway/target/release/ai-gateway`
- **Config**: `apps/ai-gateway/config.yaml`
- **Logs**: `apps/ai-gateway/gateway.log`

### Packages
- **Gateway Client**: `packages/gateway-client/src/gateway_client.py`
- **Claude Flow**: `packages/claude-flow/src/`

### Documentation
- **Main README**: `README.md`
- **Installation**: `INSTALLATION.md`
- **Guides**: `docs/guides/`
- **Reference**: `docs/reference/`
- **Development**: `docs/development/`

### Tests
- **Structure**: `test_packages_structure.py`
- **Gateway**: `test_gateway_simple.py`
- **Integration**: `test_claude_flow_integration.py`
- **Examples**: `apps/examples/`

## Troubleshooting

### "Cannot add editables to the default dependency group"

**Problem**: Trying to use `pdm add -e`

**Solution**: Use `uv pip install -e` or `pip install -e` in an activated virtual environment

```bash
# ❌ Don't do this
pdm add -e ./packages/gateway-client

# ✅ Do this instead
source .venv/bin/activate
uv pip install -e ./packages/gateway-client
```

### "No virtual environment found"

**Problem**: Trying to install without activating venv

**Solution**: Create and activate virtual environment

```bash
uv venv
source .venv/bin/activate
uv pip install -e ./packages/gateway-client
```

### "externally managed environment"

**Problem**: System Python is managed by Homebrew

**Solution**: Use virtual environment (don't install to system)

```bash
uv venv
source .venv/bin/activate
# Now install packages
```

### Import errors

**Problem**: Packages not installed or venv not activated

**Solution**: Activate venv and reinstall

```bash
source .venv/bin/activate
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow
```

### Gateway won't start

**Problem**: Port 8080 in use or API keys not loaded

**Solution**: Check port and load keys

```bash
# Check port
lsof -i :8080

# Load API keys
source ~/.zsh_secrets
echo $GROQ_API_KEY  # Should show your key
```

## API Keys Setup

Edit `~/.zsh_secrets` (or `~/.bash_secrets`):

```bash
# Required
export GROQ_API_KEY="gsk_..."
export GEMINI_API_KEY="AIza..."

# Optional
export MISTRAL_API_KEY="..."
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
```

Then load:

```bash
source ~/.zsh_secrets
```

## Quick Checks

### Verify Installation

```bash
# Check venv exists
ls .venv/

# Check packages installed (in activated venv)
python -c "from gateway_client import GatewayFactory; print('✅ gateway-client')"
python -c "from hive import Hive; print('✅ claude-flow')"

# Check gateway binary
ls apps/ai-gateway/target/release/ai-gateway

# Check API keys
echo $GROQ_API_KEY
```

### Verify Gateway Running

```bash
# Health check
curl http://localhost:8080/health

# Should return: {"status":"ok"}
```

## Package Management Summary

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **uv** | Fast Python installer | `uv pip install -e ./packages/gateway-client` |
| **pip** | Traditional Python installer | `pip install -e ./packages/gateway-client` |
| **PDM** | Project scripts | `pdm run gateway-build` |
| **pnpm** | Node.js packages | `pnpm install` |
| **cargo** | Rust packages | `cargo build --release` |

## Important Notes

1. **Always activate virtual environment** before installing packages or running Python code
2. **Don't use `pdm add -e`** - PDM can't add editable packages
3. **Use `uv pip install -e`** or `pip install -e` in activated venv
4. **Load API keys** before starting gateway: `source ~/.zsh_secrets`
5. **Virtual environment** is in `.venv/` (gitignored)

## One-Line Commands

```bash
# Full setup
pnpm install && uv venv && source .venv/bin/activate && uv pip install -e ./packages/gateway-client && uv pip install -e ./packages/claude-flow && pnpm run gateway:build

# Daily start (after setup)
source .venv/bin/activate && cd apps/ai-gateway && source ~/.zsh_secrets && ./target/release/ai-gateway --config config.yaml
```

## Documentation Links

- **Full Installation Guide**: [INSTALLATION.md](INSTALLATION.md)
- **Quick Start**: [docs/guides/QUICK_START.md](docs/guides/QUICK_START.md)
- **Testing Guide**: [docs/guides/TESTING_GUIDE.md](docs/guides/TESTING_GUIDE.md)
- **Gateway Startup**: [docs/guides/START_GATEWAY.md](docs/guides/START_GATEWAY.md)
- **Documentation Index**: [docs/README.md](docs/README.md)

---

**Need more help?** See [INSTALLATION.md](INSTALLATION.md) for detailed instructions.

