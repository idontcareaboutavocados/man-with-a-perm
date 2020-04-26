import os
import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix = os.getenv('PREFIX'))

@bot.event
async def on_ready():
    print('Death Grips Is Online')
    bot.load_extension('cogs.music')

bot.run(os.getenv('BOT_TOKEN'))