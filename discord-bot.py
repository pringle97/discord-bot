import discord
from discord.ext import commands

#initialize class as an object, defined by bot
bot = commands.Bot(command_prefix="!", case_insensitive=True)


bot.run('bot-token')