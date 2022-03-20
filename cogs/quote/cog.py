import nextcord
from nextcord.ext import commands
import requests
import urllib3
from utils.embedder import embed_success, embed_error

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Quote(commands.Cog, name="Quote"):
    """Recieves quote commands"""

    COG_EMOJI = "🗣️"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quote command ready")

    @commands.command(name="quote")
    async def quote(self, ctx, *args):
        """A command which generates random quotes from cannon

        Usage:

        ```
        $quote
        ```
        """
        try:
            data = requests.get(
                url="http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote",
                verify=False,
            ).json()
            quote = data["content"]
            await ctx.send(embed=embed_success(quote))
        except Exception as e:
            print(f"Error getting quote: {str(e)}")
            await ctx.send(
                "https://tenor.com/view/parks-and-rec-who-broke-gif-23407071"
            )
            await ctx.send(
                embed=embed_error("Don't know what you did, but you've been reported!")
            )


def setup(client):
    client.add_cog(Quote(client))
