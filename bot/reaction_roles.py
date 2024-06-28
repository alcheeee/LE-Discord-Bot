from utils import bot, reaction_roles_dict
import discord


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.message_id not in reaction_roles_dict:
        return

    message_config = reaction_roles_dict[payload.message_id]
    if payload.emoji.name not in message_config:
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = message_config[payload.emoji.name]
    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    try:
        await member.add_roles(role)
    except discord.HTTPException:
        return


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.message_id not in reaction_roles_dict:
        return

    message_config = reaction_roles_dict[payload.message_id]
    if payload.emoji.name not in message_config:
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = message_config[payload.emoji.name]
    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    try:
        await member.remove_roles(role)
    except discord.HTTPException:
        return
