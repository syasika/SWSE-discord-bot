import discord
import os
import urllib.parse
import d20
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


def get_search_url(text):
    return urllib.parse.quote_plus(text)


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


def get_roll(dice_roll_text):
    text = ""
    try:
        roll = d20.roll(dice_roll_text, stringifier=MyStringifier())
        # print(roll)
        text = f"🎲{roll}"
    except:
        return f"Something went wrong. Whoops. Check your input"

    return f"{text}"


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$search"):
        search_text = message.content.split("$search ", 1)[1]
        query = get_search_url(search_text)
        await message.channel.send(
            f"https://swse.fandom.com/wiki/Special:Search?query={query}&scope=internal"
        )

    if message.content.startswith("$roll"):
        result = get_roll(message.content.split("$roll ", 1)[1])
        await message.channel.send(result)


client.run(os.getenv("TOKEN"))
