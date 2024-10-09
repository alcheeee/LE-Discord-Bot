from typing import Any, Optional
import json
import discord
from utils import bot

class MessageHandler:
    def __init__(self, filename: str = 'messages.json'):
        self.filename = filename
        self.messages: dict[str, Any] = self.load_messages()

    def load_messages(self) -> dict[str, Any]:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_messages(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self.messages, f, indent=2)

    def get_message(self, key: str) -> str:
        return ' '.join(self.messages.get(key, ["No Message"]))

    @staticmethod
    def create(*args: str) -> str:
        return "\n".join(args)

    @staticmethod
    def create_announcement(title: str, announcement: str) -> str:
        return f"**{title}**\n\n{announcement}"

    @staticmethod
    async def respond(interaction: discord.Interaction, message: str) -> None:
        await interaction.response.send_message(message, ephemeral=True)


msg_handler = MessageHandler()
