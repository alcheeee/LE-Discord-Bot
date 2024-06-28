from utils import TOKEN, bot, common_ids, reaction_roles
import discord
from discord.ext import commands
from message_builder import BotMessage


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(name='help')
async def help_cmd(ctx):
    await ctx.send("Type !help for a list of commands")


@bot.command(name='announcement')
@commands.has_permissions(administrator=True)
async def admin_announcement(ctx, *, title: str, announcement: str):
    if ctx.author.guild_permissions.administrator:
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


@bot.command(name='post_rules')
@commands.has_permissions(manage_channels=True)
async def post_rules(ctx):
    if ctx.author.guild_permissions.manage_channels:
        rules_channel = discord.utils.get(ctx.guild.text_channels, name='rules')
        if rules_channel:
            message = await rules_channel.send(BotMessage.rules_message())
            await message.add_reaction('✅')
            reaction_roles[message.id] = {
                '✅': common_ids['member_role_id']
            }
            await ctx.send(f"Rules posted in {rules_channel.mention} and reaction role set up")
        else:
            await ctx.send("The rules channel does not exist.")
    else:
        return


@bot.command(name='post_signup')
@commands.has_permissions(manage_channels=True)
async def post_rules(ctx):
    if ctx.author.guild_permissions.manage_channels:
        sign_up_channel = discord.utils.get(ctx.guild.text_channels, name='sign-up')
        if sign_up_channel:
            message = await sign_up_channel.send(BotMessage.signup_message())
            await message.add_reaction('✅')
            reaction_roles[message.id] = {
                '✅': common_ids['contributor_role_id']
            }
            await ctx.send(f"Sign Up posted in {sign_up_channel.mention} and reaction role set up")
        else:
            await ctx.send("The sign up channel does not exist.")
    else:
        return


bot.run(TOKEN)
