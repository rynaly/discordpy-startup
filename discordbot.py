import discord
from discord.ext import commands
import asyncio
import os
import subprocess
from voice_generator import creat_WAV

client = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']
voice_client = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def join(ctx):
    print('#voicechannelを取得')
    vc = ctx.author.voice.channel
    print('#voicechannelに接続')
    await vc.connect()
    await ctx.send('よろしく')

@client.command()
async def bye(ctx):
    print('#切断')
    await ctx.voice_client.disconnect()
    await ctx.send('さよなら')

@client.event
async def on_message(message):
    msgclient = message.guild.voice_client
    if message.content.startswith('.'):
        pass

    else:
        if msgclient:
            print(message.content)
            #creat_WAV(message.content)
            await ctx.message.attachments[0].save("output.wav")
            source = discord.FFmpegPCMAudio("output.wav")
            msgclient.play(source)
        else:
            pass
    await client.process_commands(message)


client.run(token)
