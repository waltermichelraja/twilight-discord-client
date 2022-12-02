import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

client=discord.Client(intents=discord.Intents.default())
load_dotenv()
TOKEN=os.getenv("TOKEN")
client=commands.Bot(command_prefix=";")

@client.event
async def on_ready():
    print("--Twilight\'s online!--")
    try:
        sync=await client.tree.sync()
        print(f"commands synced: {len(sync)}")
    except Exception as e:
        print(e)

@client.tree.command(name="ping")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```", ephemeral=True)


client.run(TOKEN)
