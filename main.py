import discord
import os
import asyncio
import datetime, time
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv

client=discord.Client(intents=discord.Intents.default())
intents=discord.Intents.all()
client=commands.Bot(command_prefix=";", intents=intents)

load_dotenv()
TOKEN=os.getenv("TOKEN")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    print(f"--logged in as {client.user}--")
    print("------------------------------")
    global startTime
    startTime = time.time()
    try:
        sync=await client.tree.sync()
        print(f"--commands synced: {len(sync)}--")
    except Exception as e:
        print(e)

@client.tree.command(name="ping", description="sends client latency")
async def ping(interaction:discord.Interaction):
    uptime=str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed=discord.Embed(title="", description=f"```elm\nPing:   {client.latency*1000:,.0f} ms \nUptime: {uptime}```")
    start=time.time()
    await interaction.response.send_message("**Pong!**", embed=embed, ephemeral=False)
    end=time.time()
    embed=discord.Embed(title="", description=f"```elm\nPing:         {client.latency*1000:,.0f} ms \nResponseTime: {(end-start)*1000:,.0f} ms \nUptime:       {uptime}```")
    await interaction.edit_original_response(content="**Pong!**", embed=embed)


client.load_extension(f"cogs.user.py")

client.run(TOKEN)
