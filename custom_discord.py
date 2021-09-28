import discord
from config import config

TOKEN = config.TOKEN

class Client(discord.Client):
    def __init__(self, system):
        super(Client, self).__init__()
        self.system = system
    
    def run(self):
        super(Client, self).run(TOKEN)
        
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.system.reply(message)