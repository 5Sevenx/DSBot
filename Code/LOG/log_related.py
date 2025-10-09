import asyncio
from re import purge

import discord
from discord.ext import commands
from discord import Embed, guild
import datetime

from Code.CONF.config_variables import data

#Join Leave logger
class JoinLeaveLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(int(data["SPY_CHANNEL_ID"]))
        if channel:
            embed = Embed(
                title=data["NM"],
                description=data["JS"].format(member=member),
                color=0x4CBB17,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.add_field(name="Name", value=member.name, inline=True)
            embed.add_field(name="ID", value=member.id, inline=True)
            embed.add_field(
                name=data["AC"],
                value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"),
                inline=False
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(int(data["SPY_CHANNEL_ID"]))
        if channel:
            embed = Embed(
                title=data["LV"],
                description=data["LS"].format(member=member),
                color=0x808080,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.add_field(name="Name", value=member.name, inline=True)
            embed.add_field(name="ID", value=member.id, inline=True)
            await channel.send(embed=embed)
#Join Leave logger_ND

#Spy
spy_users = {}
class OnSpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spy(self,ctx,member_id:int,time:int):
        global spy_users
        guild = ctx.guild
        member = guild.get_member(member_id)
        allowed_channel_id = int(data["SPY_CHANNEL_ID"])

        if not member:
            await ctx.channel.send("Here is no user with that id")
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=2)

        if ctx.channel.id  != allowed_channel_id:
            await ctx.channel.send(data["NH"],delete_after=2)
            return

        channel = ctx.guild.get_channel(allowed_channel_id)
        spy_users[member.id] = datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
        if channel:
            embed = Embed(
                title=data["SS"],
                description=data["US"].format(member=member),
                color=0x4CBB17,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        global spy_users
        if message.author.bot:
            return

        if message.author.id in spy_users:
            if datetime.datetime.utcnow() >= spy_users[message.author.id]:
                del spy_users[message.author.id]
                return

            channel = message.guild.get_channel(int(data["SPY_CHANNEL_ID"]))
            if channel:
                embed = Embed(
                    title=data["MD"],
                    description=data["ST"].format(message=message),
                    color=0x808080,
                    timestamp=datetime.datetime.utcnow()
                )

                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        global spy_users
        if member.id not in spy_users:
            return

        if datetime.datetime.utcnow() >= spy_users[member.id]:
            channel = member.guild.get_channel(int(data["SPY_CHANNEL_ID"]))
            if channel:
                embed = Embed(
                    title=data["SE"],
                    description=data["US"].format(member=member),
                    color=0x808080,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_thumbnail(url=member.display_avatar.url)
                await channel.send(embed=embed)
            del spy_users[member.id]
            return

        channel = member.guild.get_channel(int(data["SPY_CHANNEL_ID"]))
        if not channel:
            return

        # Join VC
        if after.channel is not None and before.channel != after.channel and before.channel is None:
            embed = Embed(
                title=data["JTNC"],
                description=data["JTNCU"].format(member=member, after=after),
                color=0x808080,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)

        # Leave Vc
        elif after.channel is None and before.channel is not None:
            embed = Embed(
                title=data["LVC"],
                description=data["LVCU"].format(member=member, before=before),
                color=0x808080,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)

        # Moved between
        elif after.channel is not None and before.channel is not None and before.channel != after.channel:
            embed = Embed(
                title=data["MBVC"],
                description=data["MBVCU"].format(member=member,after=after,before=before),
                color=0x808080,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)
#Spy_ND
