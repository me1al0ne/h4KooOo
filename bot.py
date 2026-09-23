import os
import discord

TARGET_USER_ID = 1204165594581172276
RESPONSE = "گووووبخۆۆۆ"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} ({client.user.id})")

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.author.id == TARGET_USER_ID:
        try:
            await message.reply(RESPONSE, mention_author=False)
        except discord.Forbidden:
            print(f"Missing permission to reply in channel {message.channel.id}")
        except discord.HTTPException as e:
            print(f"Discord API error: {e}")

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("DISCORD_TOKEN environment variable is not set.")

client.run(token)
