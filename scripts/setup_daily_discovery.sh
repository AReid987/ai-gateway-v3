#!/bin/bash
# Setup daily model discovery cron job

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Create cron job that runs daily at 6 AM
CRON_JOB="0 6 * * * cd $PROJECT_DIR && source ~/.zsh_secrets && python3 scripts/discover_models.py >> logs/model_discovery.log 2>&1"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "✅ Daily model discovery cron job added"
echo "📅 Will run daily at 6:00 AM"
echo "📝 Logs will be saved to logs/model_discovery.log"

# Create logs directory
mkdir -p "$PROJECT_DIR/logs"

# Run initial discovery
echo "🔍 Running initial model discovery..."
cd "$PROJECT_DIR"
source ~/.zsh_secrets
python3 scripts/discover_models.py
