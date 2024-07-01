import discord
from discord.ext import commands
from discord import app_commands
from utils import EnvVars
from message_builder import bot_message
from startup import register_version_command


class base_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='sync_commands')
    @app_commands.checks.has_permissions(administrator=True)
    async def sync_commands(self, interaction: discord.Interaction):
        await register_version_command()
        await interaction.response.send_message('Version Synced.')

    @app_commands.command(name='lazy_help')
    async def help_cmd(self, interaction: discord.Interaction):
        help_message = bot_message.get_message('help')
        await interaction.response.send_message(f'Hey {interaction.user.mention},\n\n{help_message}', ephemeral=True)

    @app_commands.command(name='lazy_version')
    async def lazy_version(self, interaction: discord.Interaction):
        version_msg = f"Current Lazy Bot version is {EnvVars.VERSION}"
        await interaction.response.send_message(version_msg, ephemeral=True)

    @app_commands.command(name='lazy_announcement')
    @app_commands.checks.has_permissions(administrator=True)
    async def lazy_announcement(self, interaction: discord.Interaction, title: str, announcement: str):
        if interaction.user.guild_permissions.administrator:
            announcement_channel = discord.utils.get(interaction.guild.text_channels, name='announcements')
            if not announcement_channel:
                announcement_channel = await interaction.guild.create_text_channel('announcements')

            message = bot_message.create_announcement(title, announcement)
            await announcement_channel.send(message)
            await interaction.response.send_message("Announcement posted.", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)

    @app_commands.command(name='lazy_post')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lazy_post(self, interaction: discord.Interaction, channel_name: str, text: str):
        if interaction.user.guild_permissions.manage_channels:
            channel = discord.utils.get(interaction.guild.text_channels, name=channel_name)
            if not channel:
                await interaction.response.send_message("Channel doesn't exist", ephemeral=True)
            else:
                await channel.send(text)
                await interaction.response.send_message(f"Message posted in {channel.mention}.", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(base_cog(bot))
