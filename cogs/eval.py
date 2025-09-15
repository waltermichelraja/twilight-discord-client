import discord
import sqlite3
import io, os, sys, datetime, time, textwrap, traceback, contextlib
from discord.ext import commands

class Eval(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client=client
        self._last_result=None
        self.db=sqlite3.connect("credits.db")
        self.cursor=self.db.cursor()

    def cog_unload(self):
        if self.db:
            self.db.close()

    @staticmethod
    def cleanup_code(content: str) -> str:
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])
        return content.strip("` \n")

    def get_environment(self, ctx) -> dict:
        env={
            "discord": discord,
            "commands": commands,
            "client": self.client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "os": os,
            "sys": sys,
            "datetime": datetime,
            "time": time,
            "db": self.db,
            "cursor": self.cursor,
            "_": self._last_result,
        }
        env.update(globals())
        return env

    async def send_result(self, ctx, result: str):
        if len(result)<=1900:
            embed=discord.Embed(description=f"`Result`\n```py\n{result}\n```")
            await ctx.send(embed=embed)
        else:
            with io.StringIO(result) as file:
                await ctx.send(file=discord.File(file, "eval.txt"))

    @commands.command(aliases=["evaluate", "exe", "execute"], pass_context=True)
    @commands.is_owner()
    async def eval(self, ctx, *, body: str):
        body=self.cleanup_code(body)
        env=self.get_environment(ctx)
        stdout=io.StringIO()
        code=f"async def func():\n{textwrap.indent(body, '  ')}"
        try:
            exec(code, env)
        except Exception as e:
            return await self.send_result(ctx, f"{e.__class__.__name__}: {e}")
        func=env["func"]
        try:
            with contextlib.redirect_stdout(stdout):
                ret=await func()
        except Exception:
            value=stdout.getvalue()
            result=f"{value}{traceback.format_exc()}"
            return await self.send_result(ctx, result)
        value=stdout.getvalue()
        if ret is None:
            if value:
                await self.send_result(ctx, value)
        else:
            self._last_result=ret
            result=f"{value}{ret!r}"
            await self.send_result(ctx, result)


async def setup(client: commands.Bot):
    await client.add_cog(Eval(client))
