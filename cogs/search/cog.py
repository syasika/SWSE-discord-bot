import nextcord
from nextcord.ext import commands
import urllib.parse
from utils.embedder import embed_success


class Search(commands.Cog, name="Search"):
    """Recieves swse search commands"""

    COG_EMOJI = "🕵️"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Search command ready")

    @commands.command(name="search")
    async def search(self, ctx, *args):
        """Generates SWSE wiki search link with your search criteria

        Usage:
        ```
        $search move object
        ```
        """
        search_text = " ".join(args)
        query = get_search_url(search_text)
        await ctx.send(
            embed=embed_success(
                f"https://swse.fandom.com/wiki/Special:Search?query={query}&scope=internal"
            )
        )


def setup(client):
    client.add_cog(Search(client))


def get_search_url(text):
    return urllib.parse.quote_plus(text)
