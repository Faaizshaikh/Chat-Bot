# Slack ChatOps Deployment Bot

Automate deployments and app monitoring directly from Slack.

## Commands
- `/deploy` → Trigger GitHub Actions workflow
- `/status` → Check app health
- `/logs` → Fetch recent logs
- `/restart` → Restart app

## Setup
1. Create a Slack App → Add Slash Commands
2. Set environment variables from `.env.example`
3. Run locally:
```bash
python bot/app.py
```
