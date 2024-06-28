class BotMessage:

    @staticmethod
    def create(*args):
        return "\n".join(args)

    @staticmethod
    def create_announcement(title: str, announcement: str):
        return f"**{title}**\n\n{announcement}"


    @staticmethod
    def signup_message():
        return """
        Would you like to contribute to Lazy Extraction?
        React below to gain access to the contributor channels and help build the game!
        """


    @staticmethod
    def rules_message():
        return """
        📜 **Community Rules** 
        Welcome to the Lazy Extraction community! To ensure a positive and enjoyable environment for everyone, please follow these guidelines: 
        
        1. **Be Respectful** 
        - Treat everyone with respect. Harassment, discrimination, or hate speech will not be tolerated. 
        - Respect differing opinions and engage in discussions with civility.
        
        2. **No Spamming or Self-Promotion** 
        - Avoid spamming messages, links, or images. 
        - Self-promotion or advertising is not allowed without permission from the moderators. 
        
        3. **Keep Content Appropriate** 
        - Use appropriate language. Avoid profanity and offensive remarks. 
        - Do not share explicit, violent, or NSFW content. 
        
        5. **Respect Privacy**
        - Do not share personal information about yourself or others. 
        - Respect the privacy of other community members. 
        
        6. **Have Fun** 
        - Enjoy your time in the community and help others do the same. 
        - Encourage a positive and inclusive atmosphere. 
        
        7. **Reporting Issues** 
        - If you encounter any issues or witness rule violations, contact a moderator or use the designated reporting channels. 
        
        By following these rules, we can maintain a friendly and welcoming community for everyone. 
        If you accept the rules, react below to gain access to the community.
        
        Thank you for being a part of Lazy Extraction!
        """
