import os
import asyncio
from typing import Literal

import discord
from discord import app_commands
from utils import bot
from config import Config

from message_handler import msg_handler
from startup import load_cogs


async def clear_and_sync_commands():
    print("Clearing all commands...")
    bot.tree.copy_global_to(guild=Config.GUILD)
    await bot.tree.sync(guild=Config.GUILD)
    print("Commands cleared and synced.")


@bot.event
async def on_ready():
    activity = discord.Game(name=f'/lazy_help for commands. (WIP {Config.VERSION})')
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('------')
    print('Loaded Successfully')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print(f'Version: {Config.VERSION}')
    print('------')


@bot.tree.command(name="reload_cogs", description=f"Reloads Cogs | {Config.VERSION}")
async def reload_cogs(interaction: discord.Interaction, cog: Literal["base_cog"]):
    if interaction.user.id != int(Config.MY_USER_ID):
        await msg_handler.respond(interaction, 'No permissions')
    try:
        await bot.reload_extension(f'cogs.{cog.lower()}')
        await msg_handler.respond(interaction, f"Cogs reloaded.")
        print(f'Cogs reloaded.')
    except Exception as e:
        await msg_handler.respond(interaction, f'Failed to reload commands: {e}')


@bot.tree.command(name="reload_commands", description=f"Reloads commands | {Config.VERSION}")
async def reload_commands(interaction: discord.Interaction):
    if interaction.user.id != int(Config.MY_USER_ID):
        await msg_handler.respond(interaction, 'No permissions')
    try:
        await clear_and_sync_commands()
        await msg_handler.respond(interaction, 'Commands deleted.')
    except Exception as e:
        await msg_handler.respond(interaction, f'Failed to delete commands: {e}')


async def main():
    try:
        await load_cogs()
        if bot.get_cog('base_cog'):
            print('base_cog loaded.')
        else:
            print('base_cog not loaded.')
    except Exception as e:
        print(f'Failed to load cogs: {e}')

    await bot.start(Config.BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
