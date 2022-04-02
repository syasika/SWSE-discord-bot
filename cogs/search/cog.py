from hashlib import blake2b
import os
import nextcord
from nextcord.ext import commands
import urllib.parse
from utils.embedder import embed_success
import json


class Search(commands.Cog, name="Search"):
    """Recieves swse wiki search commands"""

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


class Feats(commands.Cog, name="Feats"):
    """Recieves swse feat search commands"""

    COG_EMOJI = "🕵️"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Feat search command ready")

    @commands.command(name="feats")
    async def search(self, ctx, *args):
        """Searches feat DB for the specified feat name. This does not include homebrew, yet.

        Usage:
        ```
        $feats acrobatic strike
        ```
        """
        search_text = " ".join(args)
        query = query_feats(search_text)
        if len(query) == 0:
            await ctx.send(
                embed=embed_success(title=f"No results found", description=f"Womp Womp")
            )

        for results in query:
            name = f"{results['name']}"
            desc = f"""Prerequisites: {results['prerequisites']}
            Description: {results['description']}
            Jedi Bonus Feat: {results['jedi']}
            Noble Bonus Feat: {results['noble']}
            Scoundrel Bonus Feat: {results['scoundrel']}
            Scout Bonus Feat: {results['scout']}
            Soldier Bonus Feat: {results['soldier']}
            """
            await ctx.send(embed=embed_success(title=name, description=desc))


class Talents(commands.Cog, name="Talents"):
    """Recieves swse talent search commands"""

    COG_EMOJI = "🕵️"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Talent search command ready")

    @commands.command(name="talents")
    async def search(self, ctx, *args):
        """Searches talent DB for the specified talent name. This does not include homebrew, yet.

        Usage:
        ```
        $talents move massive object
        ```
        """
        search_text = " ".join(args)
        query = query_talents(search_text)
        if len(query) == 0:
            await ctx.send(
                embed=embed_success(title=f"No results found", description=f"Womp Womp")
            )

        for results in query:
            name = f"{results['talent']}"
            desc = f"""Prerequisites: {results['prerequisites']}
            Class: {results['class']}
            Tree: {results['tree']}
            Benefit: {results['benefit']}
            """
            await ctx.send(embed=embed_success(title=name, description=desc))


def setup(client):
    client.add_cog(Search(client))
    client.add_cog(Feats(client))
    client.add_cog(Talents(client))


def get_search_url(text):
    return urllib.parse.quote_plus(text)


def query_feats(search):
    with open("./db/feats.json") as jsondata:
        feats = json.load(jsondata)

    results = []
    for keyval in feats:
        if search.lower() in keyval["name"].lower():
            results.append(keyval)

    return results


def query_talents(search):
    with open("./db/talents.json") as jsondata:
        feats = json.load(jsondata)

    results = []
    for keyval in feats:
        if search.lower() in keyval["talent"].lower():
            results.append(keyval)

    return results
