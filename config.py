import os

from dotenv.main import load_dotenv

load_dotenv()

# Discord config
DISCORD_TOKEN = os.getenv("TOKEN", "")
BOT_PREFIX = "$"
