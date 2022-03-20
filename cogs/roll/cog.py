from discord import Embed
import nextcord
from nextcord.ext import commands
import d20
from utils.embedder import embed_success, embed_error


class MyStringifier(d20.SimpleStringifier):
    def _str_die(self, node):
        the_rolls = []
        for val in node.values:
            inside = self._stringify(val)
            if val.number == node.size:
                inside = f"**{inside}**"
            if val.number == 1:
                inside = f"***{inside}***"
            the_rolls.append(inside)
        return ", ".join(the_rolls)

    def _str_expression(self, node):
        return (
            f"The result of the roll {self._stringify(node.roll)} was {int(node.total)}"
        )


class Roll(commands.Cog, name="Roll"):
    """Recieves dice commands"""

    COG_EMOJI = "🎲"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Roll command ready")

    @commands.command(name="roll")
    async def roll(self, ctx, arg):
        """Rolls a given amount of dice in the form _d_

        Usage:
        ```
        $roll 1d10+5
        ```
        """
        try:
            result = get_roll(arg)
            await ctx.send(embed=embed_success(result))

        except Exception as e:
            print(f"Error during roll {arg}: {str(e)}")
            await ctx.send(
                "https://tenor.com/view/parks-and-rec-who-broke-gif-23407071"
            )
            await ctx.send(
                embed=embed_error("Don't know what you did, but you've been reported!")
            )


def setup(client):
    client.add_cog(Roll(client))


def get_roll(dice_roll_text):
    text = ""
    roll = d20.roll(dice_roll_text, stringifier=MyStringifier())
    text = f"🎲{roll}"
    return f"{text}"
