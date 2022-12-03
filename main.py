import discord
import os
import datetime, time
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

intents=discord.Intents.all()
client=commands.Bot(command_prefix=";", intents=intents)
load_dotenv()
TOKEN=os.getenv("TOKEN")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print("--Twilight\'s online!--")
    global startTime
    startTime = time.time()
    try:
        sync=await client.tree.sync()
        print(f"--commands synced: {len(sync)}--")
    except Exception as e:
        print(e)


@client.tree.command(name="ping", description="sends client latency")
async def ping(interaction:discord.Interaction):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="", description=f"```yaml\nPing:   {client.latency*1000:,.0f} ms \nUptime: {uptime}```")
    await interaction.response.send_message("**Pong!**", embed=embed, ephemeral=False)


client.run(TOKEN)
