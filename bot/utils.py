from enum import Enum
import discord
from discord.ext import commands

from typing import Optional

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


class GetRole:
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    def contributor(self) -> discord.Role | None:
        return discord.utils.get(self.interaction.guild.roles, name='Contributor')

    def member(self) -> discord.Role | None:
        return discord.utils.get(self.interaction.guild.roles, name='Member')

