#!/bin/bash
# Setup Claude Flow integration with AI Gateway

echo "🚀 Setting up Claude Flow AI Gateway Integration..."

# Create Claude Flow config directory if it doesn't exist
mkdir -p ~/.claude-flow

# Copy configuration to Claude Flow directory
cp claude-flow-config.json ~/.claude-flow/ai-gateway-config.json

# Create symbolic link for easy access
ln -sf $(pwd)/claude-flow-integration.py ~/.claude-flow/ai_gateway_client.py

# Install required Python packages
pip3 install requests pyyaml

echo "✅ Claude Flow AI Gateway integration setup complete!"
echo ""
echo "📋 Usage:"
echo "  # Test the integration"
echo "  python3 claude-flow-integration.py"
echo ""
echo "  # Run example workflow"  
echo "  python3 claude-flow-workflow.py"
echo ""
echo "  # Import in your Claude Flow scripts:"
echo "  from claude_flow_integration import claude_flow_completion, claude_flow_chat"
echo ""
echo "🔧 Configuration:"
echo "  Config file: ~/.claude-flow/ai-gateway-config.json"
echo "  Gateway URL: http://localhost:8080"
echo ""
echo "⚠️  Make sure your AI Gateway is running:"
echo "  cd ai-gateway && ./target/release/ai-gateway --config config.yaml"
