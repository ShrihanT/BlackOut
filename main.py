import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '>')

@client.command(aliases=['8ball','BlackOut', 'blackout'])
async def _8ball(ctx, *, question):
    responses = [ 'It is certain.',
                  'Without a doubt.',
                  'Yes – definitely.',
                  'You may rely on it.',
                  'As I see it, yes.',
                  'Most likely.',
                  'Outlook good.',
                  'Yes.',
                  'Signs point to yes.',
                  'Reply hazy, try again.',
                  'Ask again later.',
                  'Better not tell you now.',
                  'Cannot predict now.',
                  'Concentrate and ask again.',
                  "Don't count on it.",
                  'My reply is no.',
                  'My sources say no.',
                  'Outlook not so good.',
                  'Very doubtful.']
    await ctx.send(f'\n {random.choice(responses)}')

client.run('ODUwNTM2MzQ0MDUyNTY0MDA5.YLrJsg.vIS4hjnGAXbKTgwvN09bfqv2nwQ')

