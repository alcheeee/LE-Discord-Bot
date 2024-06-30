from utils import TOKEN, bot, common_ids, reaction_roles_dict
import discord
from discord.ext import commands
from message_builder import BotMessage
import reaction_roles

bot_message = BotMessage()

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
            message = bot_message.create_announcement(title, announcement)
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
    guild = bot.get_guild(common_ids['guild_id'])

    channels_to_update = [
        ('rules_chat_id', 'rules', 'member_role_id', True),
        ('sign_up_chat_id', 'sign-up', 'contributor_role_id', True),
        ('pixel_art_chat_id', 'pixel-art', None, False),
        ('create_an_item_chat_id', 'create-an-item', None, False),
        ('quests_chat_id', 'quests', None, False)
    ]

    for channel_id_key, message_key, role_id_key, add_reaction in channels_to_update:
        await update_channel(guild, channel_id_key, message_key, role_id_key, add_reaction)

async def update_channel(guild, channel_id_key, message_key, role_id_key, add_reaction):
    channel = bot.get_channel(common_ids[channel_id_key])
    if channel:
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


bot.run(TOKEN)
