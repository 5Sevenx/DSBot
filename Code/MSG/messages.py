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
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument')
        #TODO:add more logic

        elif isinstance(error, commands.CommandNotFound):
            command = ctx.message.content[1:]
            embed = Embed(
                title=data(["CNF"]).format(command=command),
                description=data["JTSAC"],
                color=0x7F00FF
            )
            embed.add_field(name=data["L"], value=data["CHL"])
            await ctx.message.delete()
            await ctx.channel.send(embed=embed, delete_after=DeleteMSGTiming)
