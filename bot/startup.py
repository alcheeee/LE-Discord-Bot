import os
import discord
import requests
from utils import bot
from config import Config


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def register_version_command():
    help_json = {
        "name": "lazy_version",
        "type": 1,
        "description": "Check current bot version"
    }

    headers = {"Authorization": f"Bot {Config.BOT_TOKEN}"}
    response = requests.post(Config.API_URL, headers=headers, json=help_json)
    if response.status_code == 200:
        print("Command registered")
    else:
        print(f"Failed to register: {response.status_code}, {response.text}")
