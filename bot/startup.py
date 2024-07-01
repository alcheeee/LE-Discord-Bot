import discord
import requests

from message_builder import bot_message
from utils import bot, reaction_roles_dict, common_ids, EnvVars


async def clear_and_update_msgs():
    guild = bot.guilds[0] if len(bot.guilds) else None  # It'll only be in my server

    channels_to_update = [
        ('rules', 'rules', 'member_role_id', True),
        ('sign-up', 'sign-up', 'contributor_role_id', True),
        ('pixel-art', 'pixel-art', None, False),
        ('create-an-item', 'create-an-item', None, False),
        ('quests', 'quests', None, False)
    ]

    for channel_name, message_key, role_id_key, add_reaction in channels_to_update:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not channel:
            channel = await guild.create_text_channel(channel_name)
        await update_channel(channel, message_key, role_id_key, add_reaction)


async def update_channel(channel, message_key, role_id_key, add_reaction):
    await channel.purge(limit=100)
    message_data = bot_message.get_message(message_key)

    if isinstance(message_data, list):
        for part in message_data:
            message = await channel.send(part)
            if add_reaction and part == message_data[0]:
                await message.add_reaction('✅')
                reaction_roles_dict[message.id] = {
                    '✅': common_ids[role_id_key]
                }
    else:
        message = await channel.send(message_data)
        if add_reaction:
            await message.add_reaction('✅')
            reaction_roles_dict[message.id] = {
                '✅': common_ids[role_id_key]
            }


async def register_version_command():
    help_json = {
        "name": "lazy_version",
        "type": 1,
        "description": "Check current bot version"
    }

    headers = {"Authorization": f"Bot {EnvVars.BOT_TOKEN}"}
    response = requests.post(EnvVars.API_URL, headers=headers, json=help_json)
    if response.status_code == 200:
        print("Command registered")
    else:
        print(f"Failed to register: {response.status_code}, {response.text}")
