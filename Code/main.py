import asyncio
import json
import random

import discord
from discord import Embed
from discord.ext import commands
import logging

from discord.ext.commands.parameters import empty
from dotenv import load_dotenv
import os

from unicodedata import category

load_dotenv()

data_JSON = os.getenv('DATA_JSON')
data = json.loads(data_JSON)


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members= True
intents.guilds = True

#Prefix -
bot = commands.Bot(command_prefix='-', intents=intents)

#Channels id related
temp_channelsC = []
temp_channelsG = []

#Counter
cntC = 0
cntG = 0
#Counter_ND

#Channels id related_ND

#Ready
@bot.event
async def on_ready():
    print(r""" 
      :::::::::  ::::::::::     :::     :::::::::  :::   :::      ::::::::::: ::::::::          ::::::::   :::::::: 
     :+:    :+: :+:          :+: :+:   :+:    :+: :+:   :+:          :+:    :+:    :+:        :+:    :+: :+:    :+: 
    +:+    +:+ +:+         +:+   +:+  +:+    +:+  +:+ +:+           +:+    +:+    +:+        +:+        +:+    +:+  
   +#++:++#:  +#++:++#   +#++:++#++: +#+    +:+   +#++:            +#+    +#+    +:+        :#:        +#+    +:+   
  +#+    +#+ +#+        +#+     +#+ +#+    +#+    +#+             +#+    +#+    +#+        +#+   +#+# +#+    +#+    
 #+#    #+# #+#        #+#     #+# #+#    #+#    #+#             #+#    #+#    #+#        #+#    #+# #+#    #+#     
###    ### ########## ###     ### #########     ###             ###     ########          ########   ########       
    """)
#Ready_ND

#Create VC
@bot.event
async def on_voice_state_update(member, before, after):
    global cntC
    global cntG
    guild = member.guild

    # --- Chill ---
    if after.channel and after.channel.id == int(data["CHILL_CHANNEL_ID"]):
        cntC += 1
        new_channel = await guild.create_voice_channel(
            name=f'c{cntC}' ,category=after.channel.category
        )
        temp_channelsC.append(new_channel.id)
        await member.move_to(new_channel)
    # --- Chill ---

    # --- Game  ---
    elif after.channel and after.channel.id == int(data["GAME_CHANNEL_ID"]):
        cntG += 1
        new_channel = await guild.create_voice_channel(
            name=f'g{cntG}' ,category=after.channel.category
        )
        temp_channelsG.append(new_channel.id)
        await member.move_to(new_channel)
    # --- Game  ---

    # --- Game  ---
    for channel_id in temp_channelsG:
        channel = guild.get_channel(channel_id)
        if len(channel.members) == 0:
            await channel.delete()
            temp_channelsG.remove(channel_id)
            cntG -= 1
    # --- Game  ---


    # --- Chill ---
    for channel_id in temp_channelsC:
        channel = guild.get_channel(channel_id)
        if len(channel.members) == 0:
            await channel.delete()
            temp_channelsC.remove(channel_id)
            cntC -= 1
    # --- Chill ---
#Create VC_ND


@bot.command()
async def hello(ct):
    await ct.send(f'Hello {ct.author.mention}')

#Non exist command
@bot.event
async def on_message(message):
    if not message.content.startswith('-'):
        await bot.process_commands(message)
        return

    content = message.content[1:].strip()
    if not content:
        await bot.process_commands(message)
        return

    command_name = content.split()[0]

    if bot.get_command(command_name) is None:
        embed = Embed(title=f"{data["CNF"]}", description=data["JTSAC"], color=0x7F00FF)
        embed.add_field(name=data["L"], value=data["CHL"])
        await message.channel.send(embed=embed)
        await bot.process_commands(message)

    await bot.process_commands(message)

#Non exist command_ND

@bot.command()
async def roll(ctx, *args):
    message = await ctx.send("0")

    ran1, ran2 = 1, 100

    if args:
        try:
            if "-" in " ".join(args):
                parts = " ".join(args).split("-")
                ran1 = int(parts[0].strip())
                ran2 = int(parts[1].strip())
            elif len(args) == 2:  # just space
                ran1 = int(args[0])
                ran2 = int(args[1])
        except (ValueError, IndexError):
            await message.edit(content=data["EF"])
            return


    for _ in range(5):
        await asyncio.sleep(0.2)
        await message.edit(content=f" {random.randint(ran1, ran2)}")

    final = random.randint(ran1, ran2)
    await message.edit(content=f"{final}")



bot.run(data["DISCORD_TOKEN"], log_handler=handler, log_level=logging.DEBUG)