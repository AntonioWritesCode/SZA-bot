import discord
import requests
import random
import asyncio
import praw
from discord.ext.commands import Bot
from discord.ext import commands
 
client = commands.Bot(command_prefix = '.')
bot = commands.Bot(command_prefix = '$')

#Events for user joining/leaving
@client.event
async def on_ready():
    print("Sza is here on a weekend.")
 
@client.event
async def on_member_join(member):
    print(f'{member} is taking the weekend.')
 
@client.event
async def on_member_remove(member):
    print(f'{member} has lost their passport but its okay.')

#Commands for users
@client.command()
async def sza(ctx):
    await ctx.send('What')
 
@client.command(aliases=['hello'])
async def _hello(ctx, arg):
    await ctx.send(arg)

@client.command()
async def szaclear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#8ball sza
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    response = ['As I see it, yes.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don’t count on it.',
    'It is certain.',
    'It is decidedly so.',
    'Most likely.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Outlook good.',
    'Reply hazy, try again.',
    'Signs point to yes.',
    'Very doubtful.',
    'Without a doubt.'
    'Yes.',
    'Yes – definitely.',
    'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

#Bitcoin
@client.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
#Music code
#Grab music channel
@bot.command()
async def start():
    voice = await bot.join_voice_channel(channel)
    player = await voice.create_ytdl_player('https://www.youtube.com/playlist?list=PLwZYJAR6rRZVnNEeQHX-cohXu0uj3b7TM')
    player.start()


client.run('')
