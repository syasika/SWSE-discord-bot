import discord
from discord.ext import commands
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Quote(commands.Cog):
    """Recieves quote commands"""

    COG_EMOJI = "🗣️"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quote command ready")

    @commands.command()
    async def quote(self, ctx, *args):
        """A command which generates random quotes from cannon

        Usage:

        ```
        $quote
        ```
        """
        data = requests.get(
            url="http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote",
            verify=False,
        ).json()
        quote = data["content"]
        await ctx.send(quote)


def setup(client):
    client.add_cog(Quote(client))
