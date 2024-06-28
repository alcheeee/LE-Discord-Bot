import os
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)


reaction_roles = {}
common_ids = {
    # Channel IDs
    'rules_chat_id': 1255953709431787671,
    'sign_up_chat_id': 1255984831482040383,

    # Role IDs
    'contributor_role_id': 1256003684530393119,
    'member_role_id': 1255951967750983693,
}


