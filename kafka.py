import discord
import random
import os

class MyClient(discord.Client):
    """
    A custom Discord client that extends discord.Client to handle specific events and commands.
    Methods
    -------
    on_ready():
        Called when the bot has successfully connected to Discord.
    on_message(message):
        Called when a message is sent in a channel the bot has access to.
        Handles various commands and responses based on the message content.
    Commands
    --------
    - !hello: Responds with a greeting.
    - !users: Responds with the number of members in the server.
    - !bot: Responds with a custom message from the bot.
    - !bye: Responds with a goodbye message.
    - !help: Provides a list of available commands.
    - !roll [sides]: Rolls a dice with the specified number of sides (default is 10).
    - !image: Sends an image of Kafka.
    """
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        channel = str(message.channel.name)
        user_message = str(message.content)

        # Prevent the bot from responding to its own messages
        if message.author == self.user:
            return

        print(f'{username} said: "{user_message}" in ({channel})')

        # Commands
        if channel == 'bot_channel':
            if '!hello' in user_message:
                await message.channel.send(f'Hi {username}!')
            
            elif user_message == '!users':
                await message.channel.send(f'Number of Members: {len(message.guild.members)}')

            elif user_message == '!bot':
                await message.channel.send(f'Kafka here. Need something?')

            elif user_message == '!bye':
                await message.channel.send(f'Goodbye, {username}!')

            elif user_message == '!help':
                await message.channel.send("""
                **List of Commands:**
                - `!hello - get a greeting from Kafka`
                - `!users - get the number of members in the server`
                - `!bot - get a response from Kafka`
                - `!roll [sides] - roll a dice with the specified number of sides`
                - `!bye  - say goodbye to Kafka`
                - `!help  - get a little help from yours truly`
                - `!image  - show an image of Kafka`
                """)

        # Commands usable anywhere
        if '!roll' in user_message:
            try:
                parts = user_message.split()
                sides = int(parts[1]) if len(parts) > 1 else 10
                result = random.randint(1, sides)
                await message.channel.send(f"{username} rolled a {result}! 🎲")
            except ValueError:
                await message.channel.send("Please specify a valid number of sides! Example: `!roll 6`")

        if '!image' in user_message:
            try:
                image_path = r"C:\Users\msree\Downloads\kafka.png"  # Using raw string
                print(f"Image path: {image_path}")  # Debugging line to check the file path
                await message.channel.send("You want to see a pic of me? Sure, why not? Here. Don't stare at it too long.", file=discord.File(image_path))
            except Exception as e:
                print(f"Error: {e}")  # Debugging line to print the error
                await message.channel.send("I'm sorry, I can't do that right now. Please try again later.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')
