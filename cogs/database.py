import sqlite3
import discord
from discord.ext import commands
from typing import Tuple

class Database(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.con=None
        self.pointer=None

    async def connect(self):
        self.con = sqlite3.connect("credits.db")
        self.pointer = self.con.cursor()

    async def open(self, rec: Tuple=()):
        self.pointer.executemany("INSERT INTO credits VALUES(?,?)", rec)

    async def update(self, id):
        self.pointer.execute(f"UPDATE FROM credits WHERE userid={id}")

    async def close(self):
        self.con.commit()
        self.con.close()


async def setup(client)->None:
    await client.add_cog(Database(client))