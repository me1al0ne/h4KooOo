# h4KooOo

A minimal Discord bot using discord.py.

## What it does

When the Discord user with ID `1204165594581172276` sends a message in a channel where the bot can see and reply, the bot replies directly to that message with:

`گووووبخۆۆۆ`

## Setup

Set the GitHub Actions repository secret:

`DISCORD_TOKEN`

The bot requires the Discord **Message Content Intent** to be enabled in the Discord Developer Portal.

The bot also needs permission to **View Channel**, **Read Message History**, and **Send Messages** in the channels where it should respond.

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Then set `DISCORD_TOKEN` and run:

```bash
python bot.py
```
