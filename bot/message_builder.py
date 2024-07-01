import json


class BotMessage:
    def __init__(self):
        with open('messages.json', 'r') as f:
            self.messages = json.load(f)


    @staticmethod
    def create(*args):
        return "\n".join(args)

    @staticmethod
    def create_announcement(title: str, announcement: str):
        return f"**{title}**\n\n{announcement}"

    def get_message(self, key):
        return self.messages.get(key, {}).get('message', self.messages.get(key, {}).get('messages', ''))


bot_message = BotMessage()
