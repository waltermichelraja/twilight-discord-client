from datetime import datetime
from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.stat.start()
        self.utc.start()

    @tasks.loop(minutes=60, reconnect=True)
    async def stat(self):
        for guild in self.client.guilds:
          for channel in guild.channels:
            if channel.id==1047931306627039313:
              await channel.edit(name=f"Members : {len(list(filter(lambda m: not m.bot, channel.guild.members)))}")
    @stat.before_loop
    async def stat_before(self):
        await self.client.wait_until_ready()

    @tasks.loop(minutes=10, reconnect=True)
    async def utc(self):
        utc=datetime.now().strftime("%H:%M%p")
        for guild in self.client.guilds:
          for channel in guild.channels:
            if channel.id==1115360100215947327:
                await channel.edit(name = f"UTC : {utc}")
    @utc.before_loop
    async def utc_before(self):
        await self.client.wait_until_ready()

async def setup(client)-> None:
    await client.add_cog(Events(client))
