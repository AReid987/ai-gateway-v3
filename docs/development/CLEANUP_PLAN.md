# Repository Cleanup Plan

## Issues Identified

1. **Old root-level Python files** - Should be removed (now in packages/)
2. **Package management references** - Using `pip` instead of `pdm` with `uv`
3. **Test files scattered in root** - Should be organized

## Files to Remove

### Old Python Files (now in packages/)
- ✅ `gateway_client.py` - Replaced by `packages/gateway-client/src/gateway_client.py`
- ✅ `claude_flow_hive.py` - Replaced by `packages/claude-flow/src/hive.py`
- ✅ `claude_flow_swarm.py` - Replaced by `packages/claude-flow/src/swarm.py`
- ✅ `claude-flow-integration.py` - Replaced by `packages/claude-flow/src/integration.py`
- ✅ `claude-flow-workflow.py` - Replaced by `packages/claude-flow/src/workflow.py`

### Old Test Files (to be organized)
- `test_gateway.py` - Move to `apps/examples/`
- `test_claude_flow.py` - Move to `apps/examples/`
- `test_helicone.py` - Move to `apps/examples/`
- `test_helicone_gateway.py` - Move to `apps/examples/`

### Old Config/Setup Files
- `claude-flow-config.json` - No longer needed
- `setup-claude-flow.sh` - No longer needed

## Files to Update

### Documentation Files (pip → pdm/uv)
- `README.md`
- `QUICK_START.md`
- `MIGRATION_GUIDE.md`
- `PROJECT_STATUS.md`
- `TESTING_GUIDE.md`
- `STEP_4_COMPLETE.md`
- `packages/gateway-client/README.md`
- `packages/claude-flow/README.md`

### Package Files
- `package.json` - Update install:packages script
- `packages/gateway-client/setup.py` - Add note about pdm
- `packages/claude-flow/setup.py` - Add note about pdm

## PDM/UV Installation Commands

### Old (pip)
```bash
pip install -e packages/gateway-client
pip install -e packages/claude-flow
```

### New (pdm with uv)
```bash
# Install using pdm
pdm add -e ./packages/gateway-client
pdm add -e ./packages/claude-flow

# Or using uv directly
uv pip install -e packages/gateway-client
uv pip install -e packages/claude-flow
```

## Execution Order

1. ✅ Remove old Python files from root
2. ✅ Move test files to apps/examples/
3. ✅ Remove old config files
4. ✅ Update all documentation with pdm/uv commands
5. ✅ Update package.json scripts
6. ✅ Create pyproject.toml if needed

