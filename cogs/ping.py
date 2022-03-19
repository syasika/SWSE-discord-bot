import discord
from discord.ext import commands


class Ping(commands.Cog):
    """Recieves ping commands"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping command ready")

    @commands.command()
    async def ping(self, ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(Ping(client))
