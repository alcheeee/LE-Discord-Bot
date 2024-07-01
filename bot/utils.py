import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()


class EnvVars:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    VERSION = os.getenv('VERSION')
    APP_ID = os.getenv('APP_ID')

    LAZY_GUILD_ID = 1255949740646993940
    API_URL = f"https://discord.com/api/v10/applications/{APP_ID}/commands"
    GUILD_API_URL = f"https://discord.com/api/v10/applications/{APP_ID}/guilds/{LAZY_GUILD_ID}/commands"


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

reaction_roles_dict = {}
common_ids = {
    # Role IDs
    'contributor_role_id': 1256003684530393119,
    'member_role_id': 1255951967750983693,
}
