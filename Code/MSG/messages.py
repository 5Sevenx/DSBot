import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

from Code.CONF.config_variables import data

DeleteMSGTiming = 33

class MissingParameters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        command = ctx.message.content[1:]
        if command == "spy":
            allowed_channel= int(data["SPY_CHANNEL_ID"])
            if ctx.channel.id != allowed_channel:
                embed = Embed(
                title=data["FCNF"],
                description = data["JTSAC"],
                color = 0x7F00FF
                )
                embed.add_field(name=data["L"], value=data["CHL"])
                await ctx.message.delete()
                await ctx.channel.send(embed=embed, delete_after=DeleteMSGTiming)
                return


        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(
                title="Missing Argument",
                description=data["MISSA"].format(error=error, ctx=ctx),
                colour=0x7F00FF
            )
            await ctx.message.delete()
            await ctx.channel.send(embed=embed, delete_after=DeleteMSGTiming)


        elif isinstance(error, commands.CommandNotFound):

            embed = Embed(
                title=data["CNF"].format(command=command),
                description=data["JTSAC"],
                color=0x7F00FF
            )
            embed.add_field(name=data["L"], value=data["CHL"])
            await ctx.message.delete()
            await ctx.channel.send(embed=embed, delete_after=DeleteMSGTiming)

#TODO:Help command to help with commands n arguments