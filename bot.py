import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = False

bot = commands.Bot(command_prefix="!qr ", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def qr(ctx, *, text: str = None):
    if not text:
        await ctx.send("Usage: !qr <text or URL>")
        return

    qr_url = (
        "https://api.qrserver.com/v1/create-qr-code/"
        f"?size=300x300&data={quote(text)}"
    )

    embed = discord.Embed(
        title="QR Code Generated",
        description="Scan this QR code using your phone"
    )
    embed.set_image(url=qr_url)

    await ctx.send(embed=embed)



bot.run(TOKEN)