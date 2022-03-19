import discord
from discord.ext import commands
import urllib.parse


class Search(commands.Cog):
    """Recieves swse search commands"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Search command ready")

    @commands.command()
    async def search(self, ctx, *args):
        """Generates SWSE wiki search link with your search criteria ($search move object)"""
        search_text = " ".join(args)
        query = get_search_url(search_text)
        await ctx.send(
            f"https://swse.fandom.com/wiki/Special:Search?query={query}&scope=internal"
        )


def setup(client):
    client.add_cog(Search(client))


def get_search_url(text):
    return urllib.parse.quote_plus(text)
