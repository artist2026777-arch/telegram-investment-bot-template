# Telegram Investment Simulator Bot

This is a Python-based Telegram bot template that simulates investment tracking functionalities. It is designed for educational purposes to demonstrate bot structure, state management, and secure configuration.

## ⚠️ Security Warning

**NEVER commit your Telegram Bot Token to GitHub.**

The token provided in your request (`8417...`) is now compromised because it was posted publicly. You must:
1. Go to @BotFather on Telegram.
2. Revoke the current token.
3. Generate a new one.

## Deployment

### Why no GitHub Actions for Hosting?
Using GitHub Actions runners to host long-running services (like a bot running 24/7) is a **violation of GitHub's Terms of Service** and will result in your repository or account being banned. GitHub Actions is designed for CI/CD (testing and deployment), not hosting.

### Recommended Hosting Options (Free/Cheap)
1. **Railway / Render / Fly.io**: These platforms support Python apps and can run your bot 24/7.
2. **VPS (DigitalOcean, Hetzner, AWS)**: Rent a small server and run the bot using Docker or Systemd.

## Setup

1. Clone the repository.
2. Create a `.env` file based on `.env.example`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the bot: `python bot.py`.
