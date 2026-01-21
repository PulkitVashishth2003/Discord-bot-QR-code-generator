import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib.parse import quote


# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN not found. Check your .env file.")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    # This ignores messages sent by the bot itself to avoid infinite loops
    if message.author == bot.user:
        return

    print(f"I saw a message from {message.author}: {message.content}")
    
    # CRITICAL: This line allows your !qr command to still work
    await bot.process_commands(message) 
# -------------

@bot.command()
async def qr(ctx, *, text: str = None):
    """
    Generate a QR code from given text or URL
    Usage: !qr <text or URL>
    """
    if not text:
        await ctx.send("Usage: `!qr <text or URL>`")
        return

    # Generate QR code URL
    qr_url = (
        "https://api.qrserver.com/v1/create-qr-code/"
        f"?size=300x300&data={quote(text)}"
    )

    # Create embed to display QR image
    embed = discord.Embed(
        title="QR Code Generated",
        description="Scan this QR code using your phone",
        color=0x2F3136
    )
    embed.set_image(url=qr_url)
    embed.set_footer(text="Discord QR Bot")

    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)
