from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.stat.start()

    @tasks.loop(minutes=15, reconnect=True)
    async def stat(ctx, self):
        for guild in self.client.guilds:
          for channel in guild.channels:
            if channel.id==1047931306627039313:
              await channel.edit(name=f"Members: {(len([m for m in ctx.guild.members if not m.bot]))}")
    @stat.before_loop
    async def stat_before(self):
        await self.client.wait_until_ready()

async def setup(client)-> None:
    await client.add_cog(Events(client))
