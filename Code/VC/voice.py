from discord.ext import commands

from Code.CONF.config_variables import data


class OnVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Counter
        self.cntC = 0
        # Counter_ND
        self.temp_channelsC = []
    @commands.Cog.listener()
    async def on_voice_state_update(self,member, before, after):
        guild = member.guild

        # --- Chill ---
        if after.channel and after.channel.id == int(data["CHILL_CHANNEL_ID"]):
            self.cntC += 1
            new_channel = await guild.create_voice_channel(
                name=f'c{self.cntC}' ,category=after.channel.category
            )
            self.temp_channelsC.append(new_channel.id)
            await member.move_to(new_channel)
        # --- Chill ---

        # --- Chill ---
        for channel_id in self.temp_channelsC:
            channel = guild.get_channel(channel_id)
            if len(channel.members) == 0:
                await channel.delete()
                self.temp_channelsC.remove(channel_id)
                self.cntC -= 1
        # --- Chill ---