import logging
import os
import json

import discord
from dotenv import load_dotenv

load_dotenv()

data_JSON = os.getenv('DATA_JSON')
data = json.loads(data_JSON)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True