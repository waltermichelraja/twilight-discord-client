import discord
from discord import app_commands

def is_chief():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 816963491554131998  # me :)
    return app_commands.check(predicate)

class CustomCheckFailure(app_commands.CheckFailure):
    pass