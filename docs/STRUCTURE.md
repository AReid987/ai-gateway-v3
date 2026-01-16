# AI Gateway v3 - Repository Structure

**Last Updated**: 2025-10-07  
**Status**: ✅ Fully Organized and Turborepo Compliant

## Visual Structure

```
ai-gateway-v3/
│
├── 📱 apps/                          # Standalone Applications
│   ├── 🦀 ai-gateway/                # Helicone AI Gateway (Rust)
│   │   ├── Cargo.toml                # Workspace configuration
│   │   ├── config.yaml               # Gateway routing config
│   │   ├── gateway.log               # Runtime logs
│   │   ├── ai-gateway/               # Main gateway crate
│   │   ├── crates/                   # Additional crates
│   │   ├── target/release/           # Compiled binaries
│   │   │   └── ai-gateway            # Gateway executable (19MB)
│   │   └── infrastructure/           # Docker & deployment
│   │
│   ├── 📚 docs/                      # Documentation site (future)
│   │
│   └── 🧪 examples/                  # Example scripts
│       ├── test_gateway.py
│       ├── test_claude_flow.py
│       ├── test_helicone.py
│       └── test_helicone_gateway.py
│
├── 📦 packages/                      # Reusable Packages
│   ├── 🐍 gateway-client/            # Python client for AI Gateway
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   └── gateway_client.py    # Main client (v1.0.0)
│   │   ├── setup.py                  # Package installation
│   │   ├── package.json              # NPM workspace config
│   │   └── README.md                 # Package documentation
│   │
│   └── 🤖 claude-flow/               # Claude Flow Integration
│       ├── src/
│       │   ├── __init__.py
│       │   ├── integration.py        # LiteLLM-compatible
│       │   ├── hive.py               # Multi-agent Hive pattern
│       │   └── swarm.py              # Coordinated Swarm pattern
│       ├── setup.py                  # Package installation
│       ├── package.json              # NPM workspace config
│       └── README.md                 # Package documentation
│
├── 📖 docs/                          # Documentation
│   ├── README.md                     # Documentation index
│   │
│   ├── 🚀 guides/                    # User Guides
│   │   ├── QUICK_START.md            # 5-minute quick start
│   │   ├── TESTING_GUIDE.md          # Comprehensive testing
│   │   └── START_GATEWAY.md          # Gateway startup & troubleshooting
│   │
│   ├── 📚 reference/                 # Technical Reference
│   │   ├── CLAUDE.md                 # Claude AI integration
│   │   ├── GEMINI.md                 # Google Gemini integration
│   │   ├── AGENT.md                  # Agent system docs
│   │   ├── CLAUDE_FLOW_INTEGRATION.md # Claude Flow patterns
│   │   └── REUSABLE_PATTERNS.md      # Common code patterns
│   │
│   ├── 🔧 development/               # Development Logs
│   │   ├── REPOSITORY_STATUS.md      # Current status
│   │   ├── PROJECT_STATUS.md         # Project progress
│   │   ├── MIGRATION_GUIDE.md        # Migration guide
│   │   ├── CLEANUP_COMPLETE.md       # Cleanup summary
│   │   ├── STEP_4_COMPLETE.md        # Claude Flow status
│   │   ├── CLEANUP_PLAN.md           # Original cleanup plan
│   │   └── FINAL_REORGANIZATION_PLAN.md # Final structure plan
│   │
│   └── STRUCTURE.md                  # This file
│
├── 🛠️ scripts/                       # Utility Scripts
│   ├── discover_models.py            # Model discovery script
│   └── setup_daily_discovery.sh      # Cron setup script
│
├── 🧪 Root Test Files                # Easy-access tests
│   ├── test_packages_structure.py    # Package structure tests
│   ├── test_gateway_simple.py        # Simple gateway tests
│   └── test_claude_flow_integration.py # Full integration tests
│
├── ⚙️ Configuration Files
│   ├── package.json                  # NPM/PNPM workspace
│   ├── pyproject.toml                # PDM configuration
│   ├── pnpm-workspace.yaml           # PNPM workspace
│   ├── pnpm-lock.yaml                # PNPM lock file
│   └── turbo.json                    # Turborepo config
│
├── 📄 Documentation Files
│   ├── README.md                     # Main project README
│   └── REORGANIZATION_COMPLETE.md    # Reorganization summary
│
└── 📁 Other Directories
    ├── ai-gateway-v3-docs/           # External docs
    ├── goose-bench/                  # Benchmarking
    ├── logs/                         # Log files
    └── node_modules/                 # Node dependencies
```

## Directory Purposes

### 📱 apps/
**Purpose**: Standalone applications that can be deployed independently

- **ai-gateway/**: The main Rust-based AI Gateway application
- **docs/**: Future documentation site (Docusaurus, VitePress, etc.)
- **examples/**: Example scripts and integration tests

**Turborepo Convention**: ✅ Standalone apps belong here

### 📦 packages/
**Purpose**: Reusable code that can be shared across apps

- **gateway-client/**: Python client library for the AI Gateway
- **claude-flow/**: Claude Flow integration with multi-agent patterns

**Turborepo Convention**: ✅ Reusable packages belong here

### 📖 docs/
**Purpose**: All project documentation organized by category

- **guides/**: User-facing how-to guides and tutorials
- **reference/**: Technical specifications and API documentation
- **development/**: Development logs, status updates, and internal docs

**Organization**: ✅ Clean separation of documentation types

### 🛠️ scripts/
**Purpose**: Utility scripts for automation and maintenance

- Model discovery
- Cron job setup
- Other automation tasks

### 🧪 Root Test Files
**Purpose**: Quick-access test files for common testing scenarios

- Package structure verification
- Gateway health checks
- Full integration tests

**Location Rationale**: Easy to find and run from project root

## File Counts

| Directory | Files | Purpose |
|-----------|-------|---------|
| apps/ai-gateway/ | ~100+ | Main gateway application |
| apps/examples/ | 4 | Example scripts |
| packages/gateway-client/ | 5 | Python client package |
| packages/claude-flow/ | 6 | Claude Flow package |
| docs/guides/ | 3 | User guides |
| docs/reference/ | 5 | Technical docs |
| docs/development/ | 7 | Development logs |
| scripts/ | 2 | Utility scripts |
| Root tests | 3 | Test files |
| Root config | 6 | Configuration files |
| Root docs | 2 | Main documentation |

**Total Documentation Files**: 17 (organized in docs/)  
**Total Test Files**: 7 (4 in apps/examples/, 3 in root)

## Key Paths

### Gateway
```bash
apps/ai-gateway/                    # Gateway application
apps/ai-gateway/config.yaml         # Gateway configuration
apps/ai-gateway/target/release/ai-gateway  # Compiled binary
apps/ai-gateway/gateway.log         # Runtime logs
```

### Packages
```bash
packages/gateway-client/src/gateway_client.py  # Client code
packages/claude-flow/src/hive.py               # Hive pattern
packages/claude-flow/src/swarm.py              # Swarm pattern
```

### Documentation
```bash
README.md                           # Main project README
docs/README.md                      # Documentation index
docs/guides/QUICK_START.md          # Quick start guide
docs/development/PROJECT_STATUS.md  # Project status
```

### Configuration
```bash
package.json                        # NPM workspace config
pyproject.toml                      # PDM configuration
pnpm-workspace.yaml                 # PNPM workspace
turbo.json                          # Turborepo config
```

## Navigation Guide

### I want to...

**Start the gateway**
```bash
cd apps/ai-gateway
./target/release/ai-gateway --config config.yaml
```

**Build the gateway**
```bash
pnpm run gateway:build
# or
cd apps/ai-gateway && cargo build --release
```

**Install packages**
```bash
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow
```

**Run tests**
```bash
python test_packages_structure.py
python test_gateway_simple.py
python test_claude_flow_integration.py
```

**Read documentation**
```bash
# Main README
cat README.md

# Documentation index
cat docs/README.md

# Quick start
cat docs/guides/QUICK_START.md
```

**Check project status**
```bash
cat docs/development/PROJECT_STATUS.md
cat docs/development/REPOSITORY_STATUS.md
```

## Turborepo Compliance

### ✅ Follows Conventions
- Standalone apps in `apps/`
- Reusable packages in `packages/`
- Clean root directory
- Proper workspace configuration

### ✅ Benefits
- Clear separation of concerns
- Easy to scale
- Standard structure
- Better developer experience

## Maintenance

### Adding New Apps
```bash
# Create new app
mkdir apps/my-new-app

# Add to workspace (already configured)
# pnpm-workspace.yaml includes apps/*
```

### Adding New Packages
```bash
# Create new package
mkdir packages/my-new-package

# Add to workspace (already configured)
# pnpm-workspace.yaml includes packages/*
```

### Adding Documentation
```bash
# User guide
touch docs/guides/MY_GUIDE.md

# Technical reference
touch docs/reference/MY_REFERENCE.md

# Development log
touch docs/development/MY_LOG.md

# Update docs/README.md to include new file
```

## Summary

✅ **Turborepo Compliant**: Apps in apps/, packages in packages/  
✅ **Organized Documentation**: 17 files in 3 categories  
✅ **Clean Root**: Only essential files  
✅ **Easy Navigation**: Clear structure and naming  
✅ **Scalable**: Easy to add new apps/packages/docs  
✅ **Professional**: Industry-standard structure

---

**See also**: [Documentation Index](./README.md) | [Main README](../README.md)

