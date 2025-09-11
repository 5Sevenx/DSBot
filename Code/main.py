import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from unicodedata import category

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members= True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

#Channels id related

#Chill channel id
CId = int(os.getenv("CHILL_CHANNEL_ID"))
#Chill channel id_ND

#Game channel id
GId = int(os.getenv("GAME_CHANNEL_ID"))
#Game channel id_ND

temp_channelsC = []
temp_channelsG = []

#Counter
cntC = 0
cntG = 0
#Counter_ND

#Channels id related_ND


@bot.event
async def on_voice_state_update(member, before, after):
    global cntC
    guild = member.guild

    if after.channel and after.channel.id == CId:
        cntC += 1
        new_channel = await guild.create_voice_channel(
            name=f'c{cntC}' ,category=after.channel.category
        )

        temp_channelsC.append(new_channel.id)

        await member.move_to(new_channel)

    for channel_id in temp_channelsC:
        channel = guild.get_channel(channel_id)
        if len(channel.members) == 0:
            await channel.delete()
            temp_channelsC.remove(channel_id)
            cntC -= 1


bot.run(token, log_handler=handler, log_level=logging.DEBUG)