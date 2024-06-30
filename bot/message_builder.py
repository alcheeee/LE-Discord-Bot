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

    def rules_message(self):
        return self.get_message('rules')

    def signup_message(self):
        return self.get_message('sign-up')

    def pixel_art_message(self):
        return self.get_message('pixel-art')

    def create_an_item_message(self):
        return self.get_message('create-an-item')

    def quests_message(self):
        return self.get_message('quests')
