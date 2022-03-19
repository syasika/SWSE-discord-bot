import discord
from discord.ext import commands
import d20


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


class Roll(commands.Cog):
    """Recieves dice commands"""

    COG_EMOJI = "🎲"

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Roll command ready")

    @commands.command()
    async def roll(self, ctx, arg):
        """Rolls a given amount of dice in the form _d_

        Usage:
        ```
        $roll 1d10+5
        ```
        """
        result = get_roll(arg)
        await ctx.send(result)


def setup(client):
    client.add_cog(Roll(client))


def get_roll(dice_roll_text):
    text = ""
    try:
        roll = d20.roll(dice_roll_text, stringifier=MyStringifier())
        # print(roll)
        text = f"🎲{roll}"
    except:
        return "https://tenor.com/view/dude-goddamnit-cartman-you-broke-it-kyle-broflovski-stan-marsh-south-park-s6e4-gif-22001761"

    return f"{text}"
