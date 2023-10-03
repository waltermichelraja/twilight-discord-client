import sqlite3
from discord.ext import commands
from typing import Tuple

class Database(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.db = sqlite3.connect('credits.db')
        self.cursor = self.db.cursor()

    def open_credits(self, user):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS credits (userid INTEGER PRIMARY KEY, username TEXT, credits INTEGER)")
        self.cursor.execute(f"SELECT * FROM credits WHERE userid = ?", (user.id,))
        result=self.cursor.fetchone()
        if result:
            return
        if not result:
            sql = "INSERT INTO credits VALUES(?,?,?)"
            val = (user.id, user.name, 0)

            self.cursor.execute(sql, val)
            self.db.commit()

    def commit(self):
        self.db.commit()


async def setup(client)->None:
    await client.add_cog(Database(client))