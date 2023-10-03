import sqlite3

class Database():
    def __init__(self, client):
        self.client=client
        self.db = sqlite3.connect("credits.db")
        self.cursor = self.db.cursor()

    def open_credits(self, user):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS credits (userid INTEGER PRIMARY KEY, username TEXT, credits INTEGER)")
        self.cursor.execute(f"SELECT * FROM credits WHERE userid = ?", (user.id,))
        result=self.cursor.fetchone()
        if result:
            return
        if not result:
            cmd = "INSERT INTO credits VALUES(?,?,?)"
            val = (user.id, user.name, 0)

            self.cursor.execute(cmd, val)
            self.db.commit()

    def disconnect(self):
        self.cursor.close()
        self.db.close()
