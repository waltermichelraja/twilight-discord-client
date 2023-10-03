import discord
from discord import app_commands
from discord.ext import commands, tasks
from modules.database import *

class Sync(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.DB=Database(self.client)
    
    def is_chief():
        def predicate(interaction: discord.Interaction) -> bool:
            return interaction.user.id == 816963491554131998 # me :)
        return app_commands.check(predicate)

    @app_commands.command(name="sync", description="sync database")
    @is_chief()
    async def sync(self, interaction:discord.Interaction):
        try:
            for user in list(filter(lambda m: not m.bot, self.client.users)):
                self.DB.open_credits(user)
            embed=discord.Embed(description=f"`Result`\n```elm\nsuccessfully updated database...```")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            embed=discord.Embed(description=f"`Result`\n```elm\nerror: {e}```")
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(client)-> None:
    await client.add_cog(Sync(client))
