from discord import message
from custom_discord import Client
from func.Pmodoro import pomodoro

import asyncio

class Echo_system:
    def __init__(self):
        pass

    def initial_message(self):
        return "start"

    async def reply(message)->str:
        if '-P' in message.content:
            print("system pomodoro")
            await pomodoro(message)
            return


client = Client(Echo_system)
client.run()