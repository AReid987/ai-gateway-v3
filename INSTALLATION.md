# AI Gateway v3 - Installation Guide

## Package Management

This project uses **uv** for Python package management. PDM is configured for project management and scripts, but **editable installs must use uv or pip**.

### Why uv?

- ✅ **10-100x faster** than pip
- ✅ **Better dependency resolution**
- ✅ **Drop-in pip replacement**
- ✅ **Written in Rust** for performance
- ✅ **Works with PDM** for best of both worlds

## Prerequisites

### 1. Install Node.js Tools

```bash
# Install pnpm (if not already installed)
npm install -g pnpm

# Verify installation
pnpm --version
```

### 2. Install Python Tools

```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv

# Verify installation
uv --version
```

### 3. Install PDM (optional, for scripts)

```bash
# Install PDM
curl -sSL https://pdm-project.org/install-pdm.py | python3 -

# Or using pip
pip install --user pdm

# Verify installation
pdm --version
```

### 4. Install Rust (for gateway)

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verify installation
cargo --version
```

## Installation Steps

### Step 1: Clone Repository

```bash
git clone git@github.com:AReid987/ai-gateway-v3.git
cd ai-gateway-v3
```

### Step 2: Install Node.js Dependencies

```bash
pnpm install
```

### Step 3: Create Virtual Environment & Install Python Packages

#### Recommended: Using uv with virtual environment

```bash
# Create virtual environment with uv (fast!)
uv venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# Or on Windows: .venv\Scripts\activate

# Install packages
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# Or using npm script (after activating venv)
pnpm run install:packages
```

#### Alternative: Using traditional venv + pip

```bash
# Create virtual environment with Python's venv
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# Or on Windows: .venv\Scripts\activate

# Install packages
pip install -e ./packages/gateway-client
pip install -e ./packages/claude-flow

# Or using npm script (after activating venv)
pnpm run install:packages:pip
```

> **Important**: Always activate the virtual environment before installing packages or running tests!

### Step 4: Build the Gateway

```bash
# Using npm script
pnpm run gateway:build

# Or manually
cd apps/ai-gateway
cargo build --release
cd ../..
```

### Step 5: Setup API Keys

Create or edit `~/.zsh_secrets` (or `~/.bash_secrets` for bash):

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

## Verification

### Verify Python Packages

```bash
# Test package structure
python test_packages_structure.py

# Expected output:
# 🎉 ALL STRUCTURE TESTS PASSED!
```

### Verify Gateway Build

```bash
# Check if binary exists
ls -lh apps/ai-gateway/target/release/ai-gateway

# Should show a ~19MB executable
```

### Verify API Keys

```bash
# Check if keys are loaded
echo $GROQ_API_KEY
echo $GEMINI_API_KEY
```

## Common Issues

### Issue: "Cannot add editables to the default dependency group"

**Problem**: Trying to use `pdm add -e` for editable installs

**Solution**: Use `uv pip install -e` or `pip install -e` instead

```bash
# ❌ Don't do this
pdm add -e ./packages/gateway-client

# ✅ Do this instead
uv pip install -e ./packages/gateway-client
```

### Issue: "uv: command not found"

**Problem**: uv is not installed

**Solution**: Install uv

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv
```

### Issue: "cargo: command not found"

**Problem**: Rust is not installed

**Solution**: Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Issue: Import errors in Python

**Problem**: Packages not installed in editable mode

**Solution**: Reinstall packages

```bash
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow
```

## Package Management Summary

| Tool      | Purpose                              | When to Use                       |
| --------- | ------------------------------------ | --------------------------------- |
| **uv**    | Fast Python package installer        | Installing packages (recommended) |
| **pip**   | Traditional Python package installer | Installing packages (fallback)    |
| **PDM**   | Project management & scripts         | Running scripts (`pdm run ...`)   |
| **pnpm**  | Node.js package manager              | Installing Node.js deps           |
| **cargo** | Rust package manager                 | Building the gateway              |

## Installation Commands Reference

### Quick Install (Recommended)

```bash
# 1. Install Node.js dependencies
pnpm install

# 2. Install Python packages with uv
pnpm run install:packages

# 3. Build gateway
pnpm run gateway:build
```

### Manual Install

```bash
# 1. Install Node.js dependencies
pnpm install

# 2. Install Python packages
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# 3. Build gateway
cd apps/ai-gateway
cargo build --release
```

### Using PDM Scripts

```bash
# Install packages
pdm run install-packages

# Build gateway
pdm run gateway-build

# Run tests
pdm run test-structure
```

## Next Steps

After installation:

1. **Start the gateway**: See `docs/guides/START_GATEWAY.md`
2. **Run tests**: See `docs/guides/TESTING_GUIDE.md`
3. **Quick start**: See `docs/guides/QUICK_START.md`

## Development Workflow

### Daily Development

```bash
# 1. Pull latest changes
git pull

# 2. Update dependencies if needed
pnpm install
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# 3. Rebuild gateway if Rust code changed
pnpm run gateway:build

# 4. Run tests
python test_packages_structure.py
```

### Adding New Dependencies

#### Python Dependencies

```bash
# Add to package
cd packages/gateway-client
# Edit setup.py to add dependency

# Reinstall in editable mode
uv pip install -e .
```

#### Node.js Dependencies

```bash
# Add to workspace
pnpm add <package-name> -w
```

#### Rust Dependencies

```bash
# Add to Cargo.toml
cd apps/ai-gateway
cargo add <crate-name>
```

## Troubleshooting

### Check Installation Status

```bash
# Check Python packages
python -c "from gateway_client import GatewayFactory; print('✅ gateway-client installed')"
python -c "from hive import Hive; print('✅ claude-flow installed')"

# Check gateway binary
ls apps/ai-gateway/target/release/ai-gateway && echo "✅ Gateway built"

# Check API keys
[ -n "$GROQ_API_KEY" ] && echo "✅ GROQ_API_KEY set"
[ -n "$GEMINI_API_KEY" ] && echo "✅ GEMINI_API_KEY set"
```

### Clean Reinstall

```bash
# 1. Clean Python packages
pip uninstall ai-gateway-client ai-gateway-claude-flow -y

# 2. Clean Node.js
rm -rf node_modules pnpm-lock.yaml
pnpm install

# 3. Clean Rust build
cd apps/ai-gateway
cargo clean
cargo build --release
cd ../..

# 4. Reinstall Python packages
uv pip install -e ./packages/gateway-client
uv pip install -e ./packages/claude-flow

# 5. Verify
python test_packages_structure.py
```

## Summary

✅ **Use uv** for Python package installation (fast!)  
✅ **Use PDM** for running scripts (`pdm run ...`)  
✅ **Use pnpm** for Node.js dependencies  
✅ **Use cargo** for building the gateway  

**Installation Command**:
```bash
pnpm install && pnpm run install:packages && pnpm run gateway:build
```

---

**Need help?** See [docs/guides/QUICK_START.md](docs/guides/QUICK_START.md) or [docs/README.md](docs/README.md)

