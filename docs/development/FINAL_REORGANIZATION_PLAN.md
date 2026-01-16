# Final Repository Reorganization Plan

## Issues to Address

1. **Development logs scattered in root** - Need to organize markdown files
2. **ai-gateway not in apps/** - Should be `apps/ai-gateway/` per Turborepo conventions

## Proposed Structure

```
ai-gateway-v3/
├── apps/
│   ├── ai-gateway/          # MOVED from root
│   ├── docs/
│   └── examples/
│
├── packages/
│   ├── gateway-client/
│   └── claude-flow/
│
├── docs/                    # NEW - Development documentation
│   ├── development/         # Development logs
│   │   ├── CLEANUP_COMPLETE.md
│   │   ├── CLEANUP_PLAN.md
│   │   ├── MIGRATION_GUIDE.md
│   │   ├── PROJECT_STATUS.md
│   │   ├── STEP_4_COMPLETE.md
│   │   └── REPOSITORY_STATUS.md
│   ├── guides/              # User guides
│   │   ├── QUICK_START.md
│   │   ├── TESTING_GUIDE.md
│   │   └── START_GATEWAY.md
│   └── reference/           # Reference docs
│       ├── CLAUDE.md
│       ├── GEMINI.md
│       ├── AGENT.md
│       ├── CLAUDE_FLOW_INTEGRATION.md
│       └── REUSABLE_PATTERNS.md
│
├── scripts/
├── test_*.py               # Keep in root for easy access
├── package.json
├── pyproject.toml
├── README.md               # Keep in root
└── turbo.json
```

## Files to Move

### Development Logs → docs/development/
- CLEANUP_COMPLETE.md
- CLEANUP_PLAN.md
- MIGRATION_GUIDE.md
- PROJECT_STATUS.md
- STEP_4_COMPLETE.md
- REPOSITORY_STATUS.md

### User Guides → docs/guides/
- QUICK_START.md
- TESTING_GUIDE.md
- START_GATEWAY.md

### Reference Docs → docs/reference/
- CLAUDE.md
- GEMINI.md
- AGENT.md
- CLAUDE_FLOW_INTEGRATION.md
- REUSABLE_PATTERNS.md

### Main Directory → apps/ai-gateway/
- ai-gateway/ → apps/ai-gateway/

## Files to Update After Move

### Update paths in:
- package.json (all ai-gateway scripts)
- pyproject.toml (all ai-gateway scripts)
- README.md (references to ai-gateway)
- All documentation files (references to ai-gateway)
- Test scripts (if they reference ai-gateway path)

## Execution Steps

1. Create docs directory structure
2. Move development logs
3. Move user guides
4. Move reference docs
5. Move ai-gateway to apps/
6. Update all path references
7. Update documentation index
8. Test everything still works

