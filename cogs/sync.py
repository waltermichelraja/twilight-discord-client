import discord
from discord import app_commands
import datetime, time
from discord.ext import commands, tasks
from modules.database import *

class Sync(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.sync_db.start()
        #self.DB=Database(self.client)

    @tasks.loop(hours=12, reconnect=True)
    async def sync_db(self):
        try:
            start=time.time()
            for user in list(filter(lambda m: not m.bot, self.client.users)):
                DB.open_credits(user)
            end=time.time()
            print(f"=> database synced at: {datetime.datetime.utcnow()} utc; executed in: {(end-start)*1000:,.4f} ms")
        except Exception as e:
            print(description=f"=> error syncing database: {e}")
    @sync_db.before_loop
    async def sync_db_before(self):
        await self.client.wait_until_ready()


async def setup(client)-> None:
    await client.add_cog(Sync(client))
