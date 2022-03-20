import nextcord
from nextcord.ext import commands
from utils.embedder import embed_success


class Ping(commands.Cog, name="Ping"):
    """Recieves ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping command ready")

    @commands.command(name="ping")
    async def ping(self, ctx):
        """A command which simply acknowledges the user's ping.

        Usage:

        ```
        $ping
        ```
        """
        await ctx.send(
            embed=embed_success(
                title="Pong!",
                description=f"(Latency: {round(self.bot.latency * 1000)}ms)",
            )
        )


def setup(bot):
    bot.add_cog(Ping(bot))
