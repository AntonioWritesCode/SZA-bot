import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

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

#Clear Commands
@client.command()
async def szaclear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#Kick/Ban command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('NjYwNDMyMzY0MzYyNjYxOTAw.Xgf3Fw.Y2RDSSCMUKWlovAQxwT-rhfAf6E')
