import asyncio
import json
import random
import logging
import discord
import os


from discord import Embed
from discord.ext import commands

from Code.CONF.config_variables import data
from Code.RDY.ready import setup_ready
from dotenv import load_dotenv
from Code.VC.voice import on_voice
from Code.MSG.messages import non_exist_message
from Code.CMD.commands import roll_command


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members= True
intents.guilds = True

#Prefix -
bot = commands.Bot(command_prefix='-', intents=intents)

#Ready
asyncio.run(setup_ready(bot))
#Ready_ND

#Create VC
asyncio.run(on_voice(bot))
#Create VC_ND

#Non exist command
asyncio.run(non_exist_message(bot))
#Non exist command_ND

#Roll
asyncio.run(roll_command(bot))
#Roll_ND

bot.run(data["DISCORD_TOKEN"], log_handler=handler, log_level=logging.DEBUG)