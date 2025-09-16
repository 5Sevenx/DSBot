import asyncio
import random

from Code.MSG.messages import DeleteMSGTiming
from Code.CONF.config_variables import data


async def roll_command(bot):
#Roll
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
        await message.delete(delay=DeleteMSGTiming)
    #Roll_ND

