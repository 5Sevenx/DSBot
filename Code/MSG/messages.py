from discord import Embed
from Code.CONF.config_variables import data

#DeleteMSG
DeleteMSGTiming=90
#DeleteMSG_ND

async def non_exist_message(bot):
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
            await message.channel.send(embed=embed, delete_after=DeleteMSGTiming)
            await bot.process_commands(message)

        await bot.process_commands(message)
        await message.delete(delay=DeleteMSGTiming)
#Non exist command_ND