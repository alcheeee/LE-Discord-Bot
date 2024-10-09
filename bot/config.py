import os
import discord
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    VERSION: str = os.getenv('VERSION')
    APP_ID: str = os.getenv('APP_ID')

    GUILD: discord.Guild = discord.Object(id=int(os.getenv('GUILD_ID')))
    MY_USER_ID: str = os.getenv('MY_USER_ID')

    API_URL = f"https://discord.com/api/v10/applications/{APP_ID}/commands"
