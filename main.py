import os
import time
import discord
from discord.ext import commands
import GoodAnimeMemes
from webserver import keep_alive

bot = commands.Bot(command_prefix='$')

# Server info display in Console when bot runs
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("Bot is in " + str(guild_count) + " guilds.")

# Bot; when command is used, then bot starts
@bot.event
async def on_message(message):
    while message.content == "/start":
        # Obtain data
        exec(open("GoodAnimeMemes.py").read())

        # Send data 1
        print("! Downloading image...")
        await message.channel.send("hey dirtbag", file=discord.File("anime1.jpg"))
        print("Sent!")
        time.sleep(60)
        os.remove("anime1.jpg")
        # Pause bot for 4hrs (14400sec)
    else:
      pass


keep_alive()
TOKEN = os.environ['DISCORD_TOKEN']
bot.run(TOKEN)
