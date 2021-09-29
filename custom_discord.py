import discord
from discord.ext import tasks

from func.Pmodoro import pomodoro
from config import config
import asyncio

TOKEN = config.TOKEN
ID = config.ID

class Client(discord.Client):
    def __init__(self):
        self.vc_list = set()
        self.ch_list = set()
        self.loop.start()

        super(Client, self).__init__()
        self.run()
    
    def run(self):
        super(Client, self).run(TOKEN)
    
    # メッセージを受け取った時の処理
    async def on_message(self, message):
        if message.author.bot:
            return

        # メンションされたらvcに接続
        if 1 <= len(message.mentions) and str(message.mentions[0].id) == ID:
            if (message.author.voice != None):
                channel = message.author.voice.channel
                vc = await channel.connect()
                self.vc_list.add((channel, vc))
            else:
                await message.channel.send('エラー，ボイスチャンネルに入ってないよ')

        # 処理
        if ('-p' in message.content) or ('-P' in message.content) :
            for ch,vc in self.vc_list:
                if message.author.voice.channel.id == ch.id:
                    break
            await pomodoro(message, vc)
            return
    
    # 人がいないチャンネルと接続を切る
    @tasks.loop(seconds=60)
    async def loop(self):
        for ch,vc in self.vc_list:
            if len([name.id for name in ch.members]) <= 1:
                await vc.disconnect()
                self.vc_list.remove((ch,vc))
                await asyncio.sleep(1)


client = Client()