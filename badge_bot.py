import discord
from discord import app_commands
from discord.ext import commands

# Replace with your bot token
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Set up bot intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# Slash command /badge
@bot.tree.command(name="badge", description="Check your active developer badge status")
async def badge(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🎖️ Active Developer Command Used Successfully!",
        description=(
            "✅ Now please wait for **24–48 hours**.\n\n"
            "You can check your badge status at the Discord Developer website below:\n"
            "🔗 [Discord Developer Portal](https://discord.com/developers/active-developer)"
        ),
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Made by Being")
    await interaction.response.send_message(embed=embed)

# Run the bot
bot.run(TOKEN)
