import discord
from discord.ext import commands


class Ping(commands.Cog, name="Ping"):
    """Recieves ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping command ready")

    @commands.command()
    async def ping(self, ctx):
        """A command which simply acknowledges the user's ping.

        Usage:

        ```
        $ping
        ```
        """
        await ctx.send(f"Pong! (Latency: {round(self.bot.latency * 1000)}ms)")


def setup(bot):
    bot.add_cog(Ping(bot))
