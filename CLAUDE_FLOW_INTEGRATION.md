# Claude Flow AI Gateway Integration

This integration replaces LiteLLM with our AI Gateway for Claude Flow workflows, providing access to multiple free AI providers with automatic fallbacks.

## 🚀 Quick Setup

```bash
# 1. Setup the integration
./setup-claude-flow.sh

# 2. Make sure AI Gateway is running
cd ai-gateway
source ~/.zsh_secrets
./target/release/ai-gateway --config config.yaml

# 3. Test the integration
python3 claude-flow-integration.py
```

## 📋 Features

- **LiteLLM Compatible**: Drop-in replacement for LiteLLM in Claude Flow
- **Multiple Providers**: Access to Groq, Gemini, Mistral, and more
- **Automatic Fallbacks**: Switches providers when one fails
- **Free Tier Focus**: Optimized for free quota providers
- **Dynamic Discovery**: Uses daily-updated model lists

## 🔧 Usage

### Basic Completion
```python
from claude_flow_integration import claude_flow_completion

result = claude_flow_completion(
    "Analyze this code for potential issues",
    model="claude-3-haiku"
)
```

### Chat Workflow
```python
from claude_flow_integration import claude_flow_chat

messages = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi! How can I help?"},
    {"role": "user", "content": "Explain recursion"}
]

response = claude_flow_chat(messages, model="claude-3-sonnet")
```

### Workflow Class
```python
from claude_flow_workflow import AIGatewayWorkflow

workflow = AIGatewayWorkflow()

# Analyze code
analysis = workflow.analyze_code(your_code)

# Generate docs
docs = workflow.generate_documentation(your_code)

# Interactive chat
response = workflow.chat_workflow("How do I optimize this?")
```

## 🎯 Model Mapping

| Claude Flow Model | AI Gateway Model | Fallbacks |
|-------------------|------------------|-----------|
| `claude-3-sonnet` | `anthropic/claude-3-5-sonnet` | Groq Llama, Gemini |
| `claude-3-haiku` | `anthropic/claude-3-5-haiku` | Groq Llama, Gemini |
| `gpt-4` | `openai/gpt-4o-mini` | Groq Llama, Gemini |
| `llama` | `groq/llama-3.1-8b-instant` | Groq 70B, Mistral |
| `gemini` | `gemini/gemini-2.0-flash` | Gemini 1.5, Groq |

## 🔄 Automatic Fallbacks

When a model fails, the integration automatically tries:
1. Primary model from AI Gateway
2. First fallback model
3. Second fallback model
4. Returns error if all fail

## 📁 Files Created

- `claude-flow-integration.py` - Main integration client
- `claude-flow-config.json` - Configuration file
- `claude-flow-workflow.py` - Example workflow class
- `setup-claude-flow.sh` - Setup script
- `~/.claude-flow/ai-gateway-config.json` - User config

## 🚨 Troubleshooting

### Integration Not Working
```bash
# Check AI Gateway is running
curl http://localhost:8080/health

# Test integration directly
python3 claude-flow-integration.py
```

### Model Errors
- Check that your API keys are set in `~/.zsh_secrets`
- Verify models are available: `python3 scripts/discover_models.py`
- Try different model names from the mapping table

### Connection Issues
- Ensure AI Gateway is running on port 8080
- Check firewall settings
- Verify network connectivity

## 🎯 Benefits vs LiteLLM

1. **Free Focus**: Optimized for free tier providers
2. **Dynamic Models**: Daily model discovery keeps options current
3. **Better Fallbacks**: Intelligent provider switching
4. **Local Control**: No external dependencies
5. **Cost Optimization**: Maximizes free quota usage

---

**Ready to use with your existing Claude Flow workflows!**
