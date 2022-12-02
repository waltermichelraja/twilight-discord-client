import discord
import os
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv

intents=discord.Intents.all()
client=commands.Bot(command_prefix=";", intents=intents)
tree=app_commands.CommandTree(client)
load_dotenv()
TOKEN=os.getenv("TOKEN")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print("--Twilight\'s online!--")
    try:
        sync=await client.tree.sync()
        print(f"--commands synced: {len(sync)}--")
    except Exception as e:
        print(e)


@tree.context_menu(name="ping", description="sends client latency")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```", ephemeral=True)


client.run(TOKEN)
