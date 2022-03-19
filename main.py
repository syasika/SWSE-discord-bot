from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(os.getenv("TOKEN"))
