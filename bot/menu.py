import discord
from message_handler import msg_handler
from discord import ButtonStyle, Interaction
from discord.ui import Button


class ContributeView(discord.ui.View):
	def __init__(self):
		super().__init__()

	@discord.ui.button(label="Pixel-Art", style=ButtonStyle.primary, emoji="🎨")
	async def pixel_art(self, interaction: Interaction, button: Button):
		message = message_handler.get_message('pixel-art')
		await message_handler.respond(interaction, message)

	@discord.ui.button(label="Quests", style=ButtonStyle.success, emoji="📜")
	async def quests(self, interaction: Interaction, button: Button):
		message = message_handler.get_message('quests')
		await message_handler.respond(interaction, message)

	@discord.ui.button(label="Items", style=ButtonStyle.danger, emoji="🛠️")
	async def items(self, interaction: Interaction, button: Button):
		view = ItemContributeView()
		await interaction.response.send_message("Select an item type to contribute:", view=view, ephemeral=True)


class ItemContributeView(discord.ui.View):
	def __init__(self):
		super().__init__()

	@discord.ui.button(label="Weapon", style=ButtonStyle.primary, emoji="🔫")
	async def weapon(self, interaction: Interaction, button: Button):
		message = message_handler.get_message('create-a-weapon')
		await message_handler.respond(interaction, message)

	@discord.ui.button(label="Attachments", style=ButtonStyle.success, emoji="🔧")
	async def attachments(self, interaction: Interaction, button: Button):
		message = message_handler.get_message('create-an-attachment')
		await message_handler.respond(interaction, message)

	@discord.ui.button(label="Armor", style=ButtonStyle.danger, emoji="🛡️")
	async def armor(self, interaction: Interaction, button: Button):
		message = message_handler.get_message('create-armor')
		await message_handler.respond(interaction, message)
