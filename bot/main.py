import os
import asyncio
from typing import Literal

import discord
from discord import app_commands

from utils import EnvVars, bot
from message_builder import bot_message
import reaction_roles
from startup import clear_and_update_msgs


cogs = ['base_cog']

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded {filename[:-3]}.py")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    # Activity
    activity = discord.Game(name=f'/lazy_help for commands. (WIP {EnvVars.VERSION})')
    await bot.change_presence(status=discord.Status.online, activity=activity)

    # Startup
    await bot.tree.sync()
    await clear_and_update_msgs()


@bot.tree.command(name="reload_cogs", description="Reloads Cogs")
@app_commands.checks.has_permissions(administrator=True)
async def reload_cogs(interaction: discord.Interaction, cog: Literal["base_cog"]):
    try:
        await bot.reload_extension(name='cogs.' + cog.lower())
        await interaction.response.send_message(f"Cogs reloaded.")
        print(f'Cogs reloaded.')

    except Exception as e:
        await interaction.response.send_message(f'Failed to reload commands: {e}', ephemeral=True)
    await interaction.response.send_message('Commands reloaded.', ephemeral=True)


async def main():
    try:
        await load_cogs()
        cog = bot.get_cog('base_cog')
        if cog:
            print('base_cog loaded.')
        else:
            print('base_cog not loaded.')

    except Exception as e:
        print(f'Failed to load cogs: {e}')

    await bot.start(EnvVars.BOT_TOKEN)


asyncio.run(main())
