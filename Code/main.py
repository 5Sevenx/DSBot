import asyncio


from discord.ext import commands

from Code.CMD.commands import RollCommand, DeleteMessages
from Code.CONF.config_variables import data, intents
from Code.LOG.log_related import JoinLeaveLogger, OnSpy
from Code.MSG.messages import MissingParameters
from Code.RDY.ready import RDY
from Code.VC.voice import OnVoice

bot = commands.Bot(command_prefix='-', intents=intents)

async def main():
    #Ready
    await bot.add_cog(RDY(bot))
    #Ready_ND

    await bot.add_cog(MissingParameters(bot))

    await bot.add_cog(RollCommand(bot))

    await bot.add_cog(DeleteMessages(bot))

    await bot.add_cog(OnVoice(bot))

    await bot.add_cog(OnSpy(bot))

    await bot.add_cog(JoinLeaveLogger(bot))

    await bot.start(data["DISCORD_TOKEN"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(r"""
           ░███████   ░██                      ░██        ░██                   ░██ 
           ░██   ░██                           ░██        ░██                   ░██ 
           ░██    ░██ ░██ ░███████   ░██████   ░████████  ░██  ░███████   ░████████ 
           ░██    ░██ ░██░██              ░██  ░██    ░██ ░██ ░██    ░██ ░██    ░██ 
           ░██    ░██ ░██ ░███████   ░███████  ░██    ░██ ░██ ░█████████ ░██    ░██ 
           ░██   ░██  ░██       ░██ ░██   ░██  ░███   ░██ ░██ ░██        ░██   ░███ 
           ░███████   ░██ ░███████   ░█████░██ ░██░█████  ░██  ░███████   ░█████░██                                                                                                                         
           """)
