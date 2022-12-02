import discord
#import asyncio
import os
from discord import app_commands
from dotenv import load_dotenv

class MyClient(discord.Client):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=855003897138774048))
        print("--Twilight\'s online--")
    
client=MyClient(intents=discord.Intents.default())
tree=app_commands.CommandTree(client)
load_dotenv()
TOKEN=os.getenv("TOKEN")

@tree.context.menu(name="ping")
async def ping(interaction:discord.Interaction,message=discord.Message):
    await interaction.response.send_message(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```")


client.run(TOKEN)
