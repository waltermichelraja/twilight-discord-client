import discord
from discord import app_commands
from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, client):
        self.client=client

    @app_commands.command(name="sync", description="sync database")
    @app_commands.
    async def sync(self, interaction:discord.Interaction):
        try:
          for user in list(filter(lambda m: not m.bot, self.client.users)):
            self.DB.open_credits(user)
          self.DB.commit()
          embed=discord.Embed(description=f"`Result`\n```elm\nsuccessfully updated database...")
          await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
          embed=discord.Embed(description=f"`Result`\n```elm\nerror: {e}")
          await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(client)-> None:
    await client.add_cog(Events(client))
