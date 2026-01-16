# How to Start the AI Gateway

## Prerequisites

1. **Build the gateway** (if not already built):
   ```bash
   cd ai-gateway
   cargo build --release
   ```

2. **Set up API keys** in `~/.zsh_secrets`:
   ```bash
   export GROQ_API_KEY="gsk_..."
   export GEMINI_API_KEY="AIza..."
   export MISTRAL_API_KEY="..."
   export ANTHROPIC_API_KEY="sk-ant-..."
   export OPENAI_API_KEY="sk-..."
   ```

## Starting the Gateway

### Option 1: Direct Command
```bash
cd ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml
```

### Option 2: Using npm script
```bash
# Make sure you're in the project root
pnpm run gateway:start
```

### Option 3: Development Mode (with auto-reload)
```bash
pnpm run gateway:dev
```

## Verifying the Gateway is Running

### 1. Health Check
```bash
curl http://localhost:8080/health
```

Expected output:
```json
{"status":"ok"}
```

### 2. Test Chat Completion
```bash
curl -X POST http://localhost:8080/ai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "groq/llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 50
  }'
```

### 3. Run the Simple Test Script
```bash
python test_gateway_simple.py
```

## Troubleshooting

### Gateway won't start
- **Check if port 8080 is already in use:**
  ```bash
  lsof -i :8080
  ```
- **Check if the binary exists:**
  ```bash
  ls -lh ai-gateway/target/release/ai-gateway
  ```
- **Rebuild if necessary:**
  ```bash
  cd ai-gateway && cargo build --release
  ```

### API Keys not loaded
- **Verify keys are set:**
  ```bash
  source ~/.zsh_secrets
  echo $GROQ_API_KEY
  ```
- **Check the secrets file exists:**
  ```bash
  cat ~/.zsh_secrets | grep API_KEY
  ```

### Requests failing
- **Check gateway logs:**
  ```bash
  tail -f ai-gateway/gateway.log
  ```
- **Verify config.yaml is correct:**
  ```bash
  cat ai-gateway/config.yaml
  ```
- **Test with different models:**
  - Try `groq/llama-3.1-8b-instant` (usually has free quota)
  - Try `gemini/gemini-2.0-flash` (Google's free tier)
  - Try `mistral/mistral-small` (Mistral's free tier)

## Common Issues

### Issue: "RouteType not found" or requests not registering

This usually means the gateway is not properly parsing the request path. The gateway expects requests in one of these formats:

1. **Unified API** (recommended):
   ```
   POST /ai/chat/completions
   ```

2. **Router-specific**:
   ```
   POST /router/{router-id}/chat/completions
   ```

3. **Direct proxy**:
   ```
   POST /{provider}/chat/completions
   ```

Make sure your requests use the `/ai/` prefix for unified API routing.

### Issue: Build fails with "edition2024" error

This has been fixed! The workspace now uses `edition = "2021"` instead of `"2024"`.

If you still see this error:
```bash
cd ai-gateway
cargo clean
cargo build --release
```

## Next Steps

Once the gateway is running:
1. Test with the simple test script: `python test_gateway_simple.py`
2. Try the Claude Flow integration: `python -m claude_flow.integration`
3. Explore the packages: `packages/gateway-client/` and `packages/claude-flow/`

