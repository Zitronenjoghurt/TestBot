import discord
from discord.ext import commands
from src.constants.config import Config
from src.utils.command_operations import get_extensions

CONFIG = Config.get_instance()

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())

@bot.event
async def on_ready():
    extensions = get_extensions()
    for extension in extensions:
        await bot.load_extension(extension)
    print(f'Logged in as {bot.user.name}')

bot.run(CONFIG.BOT_TOKEN)