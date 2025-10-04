from discord import Embed
from discord.ext import commands
from Code.CONF.config_variables import data

DeleteMSGTiming = 300

class NonExistMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.content.startswith('-'):
            return

        command_name = message.content[1:].split()[0]
        cmd = self.bot.get_command(command_name)

        if cmd is None:
            embed = Embed(
                title=data["CNF"].format(command=command_name),
                description=data["JTSAC"],
                color=0x7F00FF
            )
            embed.add_field(name=data["L"], value=data["CHL"])
            await message.channel.send(embed=embed, delete_after=DeleteMSGTiming)

#TODO:Error handler. if i got correct command but wrong parameters