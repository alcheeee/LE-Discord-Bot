from enum import Enum
import discord
from discord.ext import commands
from discord import app_commands, Interaction
from config import Config
from menu import ContributeView
from message_handler import msg_handler
from startup import register_version_command
from utils import GetRole, bot


class base_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name='sync_version', description=f"Registers Version command | {Config.VERSION}")
    @app_commands.checks.has_permissions(administrator=True)
    async def sync_commands(self, interaction: Interaction):
        await register_version_command()
        await msg_handler.respond(interaction, 'Version Synced.')


    @app_commands.command(name='lazy_help', description=f"Help command | {Config.VERSION}")
    async def help_cmd(self, interaction: Interaction):
        help_message = msg_handler.get_message('help')
        await msg_handler.respond(interaction, f'Hey {interaction.user.mention},\n\n{help_message}')


    @app_commands.command(name='lazy_version', description=f"Get Version | {Config.VERSION}")
    async def lazy_version(self, interaction: Interaction):
        version_msg = f"Current Lazy Bot version is {Config.VERSION}"
        await msg_handler.respond(interaction, version_msg)


    @app_commands.command(name='lazy_announcement', description=f"Post announcement | {Config.VERSION}")
    @app_commands.checks.has_permissions(administrator=True)
    async def lazy_announcement(self, interaction: Interaction, title: str, announcement: str):
        announcement_channel = await self.get_or_create_channel(interaction.guild, 'announcements')
        message = msg_handler.create_announcement(title, announcement)
        await announcement_channel.send(message)
        await msg_handler.respond(interaction, "Announcement posted.")


    @app_commands.command(name='lazy_post', description=f"Post in a channel | {Config.VERSION}")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lazy_post(self, interaction: Interaction, channel_name: str, text: str):
        channel = discord.utils.get(interaction.guild.text_channels, name=channel_name)
        if not channel:
            await msg_handler.respond(interaction, "Channel doesn't exist")

        await channel.send(text)
        await msg_handler.respond(interaction, f"Message posted in {channel.mention}.")


    @app_commands.command(name='contribute', description="Get templates to contribute to Lazy Extraction")
    async def get_contribution_template(self, interaction: Interaction):
        contributor_role = GetRole(interaction).contributor()
        if contributor_role not in interaction.user.roles:
            message = "Use the `/become-a-contributor` command to contribute, thank you for your interest!"
            await msg_handler.respond(interaction, message)

        view = ContributeView()
        await interaction.response.send_message("Choose an option:", view=view, ephemeral=True)


    @app_commands.command(name='become-a-contributor', description="Use this command to get the Contributor Role, or remove it")
    async def become_a_contributor(self, interaction: Interaction):
        try:
            contributor_role = GetRole(interaction).contributor()
            if contributor_role in interaction.user.roles:
                await interaction.user.remove_roles(contributor_role)
                await msg_handler.respond(interaction, "Contributor role removed.")
            else:
                await interaction.user.add_roles(contributor_role)
                message = (
                    "Thank you for your interest in wanting to contribute to Lazy Extraction!",
                    "Your input is extremely valuable to the community."
                )
                await msg_handler.respond(interaction, ' '.join(message))
        except Exception as e:
            print(str(e))
            await msg_handler.respond(interaction, "An error occured, please try again later")


    @staticmethod
    async def get_or_create_channel(guild: discord.Guild, channel_name: str) -> discord.TextChannel:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not channel:
            channel = await guild.create_text_channel(channel_name)
        return channel


async def setup(bot):
    await bot.add_cog(base_cog(bot))
