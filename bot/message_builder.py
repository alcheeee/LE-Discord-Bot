class BotMessage:

    @staticmethod
    def create(*args):
        return "\n".join(args)

    @staticmethod
    def create_announcement(title: str, announcement: str):
        return f"**{title}**\n\n{announcement}"


    @staticmethod
    def signup_message():
        return (
            "Would you like to contribute to Lazy Extraction?\n"
            "React below to gain access to the contributor channels and help build the game!"
        )


    @staticmethod
    def rules_message():
        return (
            "📜 **Community Rules**\n"
            "Welcome to the Lazy Extraction community! To ensure a positive and enjoyable environment for everyone, please follow these guidelines:\n\n"
            "1. **Be Respectful**\n"
            "   - Treat everyone with respect. Harassment, discrimination, or hate speech will not be tolerated.\n"
            "   - Respect differing opinions and engage in discussions with civility.\n\n"
            "2. **No Spamming or Self-Promotion**\n"
            "   - Avoid spamming messages, links, or images.\n"
            "   - Self-promotion or advertising is not allowed without permission from the moderators.\n\n"
            "3. **Keep Content Appropriate**\n"
            "   - Use appropriate language. Avoid profanity and offensive remarks.\n"
            "   - Do not share explicit, violent, or NSFW content.\n\n"
            "5. **Respect Privacy**\n"
            "   - Do not share personal information about yourself or others.\n"
            "   - Respect the privacy of other community members.\n\n"
            "6. **Have Fun**\n"
            "   - Enjoy your time in the community and help others do the same.\n"
            "   - Encourage a positive and inclusive atmosphere.\n\n"
            "7. **Reporting Issues**\n"
            "   - If you encounter any issues or witness rule violations, contact a moderator or use the designated reporting channels.\n\n"
            "By following these rules, we can maintain a friendly and welcoming community for everyone.\n"
            "If you accept the rules, react below to gain access to the community.\n\n"
            "Thank you for being a part of Lazy Extraction!"
        )
