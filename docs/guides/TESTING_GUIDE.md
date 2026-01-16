# AI Gateway v3 - Testing Guide

## Overview

This guide explains how to test the AI Gateway v3 and Claude Flow integration.

## Test Levels

### Level 1: Package Structure (No Gateway Required) ✅

**Test**: `test_packages_structure.py`

**What it tests:**
- Package imports work correctly
- All files are in the right locations
- Package metadata is accessible
- Dependencies are installed

**How to run:**
```bash
python3 test_packages_structure.py
```

**Expected result:**
```
🎉 ALL STRUCTURE TESTS PASSED!
Packages are correctly installed and structured.
```

**Status**: ✅ PASSING (5/5 tests)

---

### Level 2: Gateway Health (Gateway Required) ⏳

**Test**: `test_gateway_simple.py`

**What it tests:**
- Gateway is running and healthy
- Basic chat completion works
- Gateway client can connect

**Prerequisites:**
1. Build the gateway:
   ```bash
   cd ai-gateway
   cargo build --release
   ```

2. Load API keys:
   ```bash
   source ~/.zsh_secrets
   ```

3. Start the gateway:
   ```bash
   cd ai-gateway
   ./target/release/ai-gateway --config config.yaml
   ```

**How to run** (in another terminal):
```bash
python3 test_gateway_simple.py
```

**Expected result:**
```
✅ Gateway is healthy!
✅ Chat completion successful!
   Response: Gateway working!
```

**Status**: ⏳ Ready to test

---

### Level 3: Full Integration (Gateway Required) ⏳

**Test**: `test_claude_flow_integration.py`

**What it tests:**
- Gateway connection
- Gateway client package
- Claude Flow integration functions
- Hive pattern (multi-agent collaboration)
- Swarm pattern (coordinated hives)
- Pre-configured research hive

**Prerequisites:**
Same as Level 2 (gateway must be running)

**How to run:**
```bash
python3 test_claude_flow_integration.py
```

**Expected result:**
```
🎉 ALL TESTS PASSED! Claude Flow integration is working!

Total Tests: 6
✅ Passed: 6
❌ Failed: 0
```

**Status**: ⏳ Ready to test

---

## Troubleshooting

### Gateway Won't Start

**Problem**: Port 8080 already in use
```bash
# Check what's using port 8080
lsof -i :8080

# Kill the process if needed
kill -9 <PID>
```

**Problem**: Cargo build fails
```bash
# Clean and rebuild
cd ai-gateway
cargo clean
cargo build --release
```

**Problem**: API keys not loaded
```bash
# Check if keys are set
echo $GROQ_API_KEY
echo $GEMINI_API_KEY

# Load them
source ~/.zsh_secrets
```

### Tests Failing

**Problem**: Import errors
```bash
# Reinstall packages using pdm (recommended)
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow

# Or using uv
uv pip install -e packages/gateway-client
uv pip install -e packages/claude-flow
```

**Problem**: Connection refused
```bash
# Make sure gateway is running
curl http://localhost:8080/health

# Check gateway logs
tail -f ai-gateway/gateway.log
```

**Problem**: 404 errors
- Make sure you're using `/ai/chat/completions` not `/v1/chat/completions`
- Check the router configuration in `ai-gateway/config.yaml`

### Gateway Logs

**View logs:**
```bash
tail -f ai-gateway/gateway.log
```

**Enable debug logging:**
Edit `ai-gateway/config.yaml`:
```yaml
telemetry:
  level: debug
```

---

## Test Workflow

### Quick Test (2 minutes)
```bash
# 1. Test package structure
python3 test_packages_structure.py

# Expected: All 5 tests pass
```

### Full Test (5 minutes)
```bash
# 1. Build gateway (if not already built)
cd ai-gateway && cargo build --release && cd ..

# 2. Start gateway (in one terminal)
cd ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml

# 3. Run tests (in another terminal)
python3 test_gateway_simple.py
python3 test_claude_flow_integration.py
```

---

## Manual Testing

### Test Gateway Client

```python
from gateway_client import GatewayFactory

# Create client
client = GatewayFactory.balanced()

# Test request
response = client.chat_completion(
    model="groq/llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Say hello!"}],
    max_tokens=50
)

print(response['choices'][0]['message']['content'])
```

### Test Hive Pattern

```python
import asyncio
import sys
from pathlib import Path

# Add packages to path
sys.path.insert(0, str(Path.cwd() / "packages" / "claude-flow" / "src"))

from hive import Hive

async def test_hive():
    hive = Hive("test")
    hive.add_agent("agent1", "a helpful assistant")
    
    results = await hive.collaborate("What is AI?")
    
    for name, result in results.items():
        print(f"{name}: {result}")

asyncio.run(test_hive())
```

### Test Swarm Pattern

```python
import asyncio
import sys
from pathlib import Path

# Add packages to path
sys.path.insert(0, str(Path.cwd() / "packages" / "claude-flow" / "src"))

from swarm import Swarm
from hive import Hive

async def test_swarm():
    swarm = Swarm("test-swarm")
    
    # Add hive
    hive = Hive("team1")
    hive.add_agent("agent1", "a researcher")
    swarm.add_hive(hive)
    
    # Execute mission
    results = await swarm.execute_mission("Research quantum computing")
    
    print(f"Mission: {results['mission']}")
    print(f"Results: {results['results']}")

asyncio.run(test_swarm())
```

---

## Test Coverage

### ✅ Covered
- Package structure and imports
- Gateway client functionality
- Basic chat completions
- Hive pattern
- Swarm pattern
- Integration functions

### ⏳ To Be Added
- Unit tests for individual functions
- Error handling tests
- Rate limiting tests
- Fallback routing tests
- Multi-model tests
- Performance tests

---

## CI/CD Integration (Future)

### GitHub Actions Workflow

```yaml
name: Test AI Gateway

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Install Rust
      uses: actions-rs/toolchain@v1
      with:
        toolchain: stable
    
    - name: Install Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install packages
      run: |
        pip install uv
        uv pip install -e packages/gateway-client
        uv pip install -e packages/claude-flow
    
    - name: Test package structure
      run: python3 test_packages_structure.py
    
    - name: Build gateway
      run: cd ai-gateway && cargo build --release
    
    - name: Start gateway
      run: |
        cd ai-gateway
        ./target/release/ai-gateway --config config.yaml &
        sleep 5
    
    - name: Run integration tests
      env:
        GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
        GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
      run: python3 test_claude_flow_integration.py
```

---

## Summary

| Test Level  | Script                            | Gateway Required | Status    |
| ----------- | --------------------------------- | ---------------- | --------- |
| Structure   | `test_packages_structure.py`      | ❌ No             | ✅ Passing |
| Health      | `test_gateway_simple.py`          | ✅ Yes            | ⏳ Ready   |
| Integration | `test_claude_flow_integration.py` | ✅ Yes            | ⏳ Ready   |

**Next Step**: Start the gateway and run the integration tests!

```bash
# Terminal 1: Start gateway
cd ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml

# Terminal 2: Run tests
python3 test_gateway_simple.py
python3 test_claude_flow_integration.py
```

