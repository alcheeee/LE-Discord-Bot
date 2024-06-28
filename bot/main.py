from utils import TOKEN, bot, common_ids, reaction_roles_dict
import discord
from discord.ext import commands
from message_builder import BotMessage
import reaction_roles


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    await clear_and_recreate_channels()


@bot.command(name='LE_help')
async def help_cmd(ctx):
    await ctx.send("Type !LE_help for a list of commands")


@bot.command(name='post_announcement')
@commands.has_permissions(administrator=True)
async def admin_announcement(ctx, *, content: str):
    if ctx.author.guild_permissions.administrator:
        parts = content.split('|', 1)
        title, announcement = parts
        announcement_channel = discord.utils.get(ctx.guild.text_channels, name='announcements')
        if announcement_channel:
            message = BotMessage.create_announcement(title, announcement)
            await announcement_channel.send(message)
        else:
            await ctx.send("The announcements channel does not exist.")
    else:
        return


@bot.command(name='post')
@commands.has_permissions(manage_channels=True)
async def bot_post(ctx, channel: discord.TextChannel, *, text: str):
    if ctx.author.guild_permissions.administrator:
        await channel.send(text)
    else:
        return


async def clear_and_recreate_channels():
    guild = bot.get_guild(1255949740646993940)

    # Clear rules channel
    rules_channel = bot.get_channel(common_ids['rules_chat_id'])
    if rules_channel:
        await rules_channel.purge(limit=100)
        rules_message = await rules_channel.send(BotMessage.rules_message())
        await rules_message.add_reaction('✅')
        reaction_roles_dict[rules_message.id] = {
            '✅': common_ids['member_role_id']
        }

    # Clear sign-up channel
    sign_up_channel = bot.get_channel(common_ids['sign_up_chat_id'])
    if sign_up_channel:
        await sign_up_channel.purge(limit=100)
        signup_message = await sign_up_channel.send(BotMessage.signup_message())
        await signup_message.add_reaction('✅')
        reaction_roles_dict[signup_message.id] = {
            '✅': common_ids['contributor_role_id']
        }


bot.run(TOKEN)
