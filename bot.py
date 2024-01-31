import discord
from discord.ext import commands
from src.constants.config import Config

CONFIG = Config.get_instance()

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())

bot.run(CONFIG.BOT_TOKEN)