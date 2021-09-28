import discord

async def chaimu(message,vc):
    if (message.author.voice != None):
        if vc != None:
            vc.play(discord.FFmpegPCMAudio('nc.mp3'))