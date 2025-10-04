import asyncio
import random
from discord.ext import commands
from Code.MSG.messages import DeleteMSGTiming
from Code.CONF.config_variables import data

class RollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, *args):
        await ctx.message.delete(delay=DeleteMSGTiming)
        msg = await ctx.send("0")
        ran1, ran2 = 1, 100

        if args:
            try:
                if "-" in " ".join(args):
                    parts = " ".join(args).split("-")
                    ran1 = int(parts[0].strip())
                    ran2 = int(parts[1].strip())
                elif len(args) == 2:
                    ran1 = int(args[0])
                    ran2 = int(args[1])
            except (ValueError, IndexError):
                await msg.edit(content=data["EF"])
                return

        for _ in range(5):
            await asyncio.sleep(0.2)
            await msg.edit(content=f"{random.randint(ran1, ran2)}")

        final = random.randint(ran1, ran2)
        await msg.edit(content=f"{final}")
        await msg.delete(delay=DeleteMSGTiming)
