import discord
from discord import app_commands
from discord.ext import commands, tasks

class User(commands.Cog):
    def __init__(self, client):
        self.client=client
    async def on_ready(self):
        await self.client.tree.sync()

    @app_commands.CommandTree.command(name="cog", description="cog test")
    async def cog(self, interaction:discord.Interaction):
        await interaction.response.send_message("hello!", ephemeral=True)

async def setup(client):
    await client.add_cog(User(client))