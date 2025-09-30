from discord.ext import commands
from discord import Embed
import datetime

from Code.CONF.config_variables import data


class JoinLeaveLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(1422182199112761434)
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
        channel = member.guild.get_channel(1422182295200075868)
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
