from discord.ext import commands

from Code.CONF.config_variables import data

#Channels id related_ND
class OnVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Counter
        self.cntC = 0
        self.cntG = 0
        # Counter_ND
        self.temp_channelsC = []
        self.temp_channelsG = []
    @commands.Cog.listener()
    async def on_voice_state_update(self,member, before, after):
        global cntC
        global cntG
        guild = member.guild

        # --- Chill ---
        if after.channel and after.channel.id == int(data["CHILL_CHANNEL_ID"]):
            cntC += 1
            new_channel = await guild.create_voice_channel(
                name=f'c{cntC}' ,category=after.channel.category
            )
            self.temp_channelsC.append(new_channel.id)
            await member.move_to(new_channel)
        # --- Chill ---

        # --- Game  ---
        elif after.channel and after.channel.id == int(data["GAME_CHANNEL_ID"]):
            cntG += 1
            new_channel = await guild.create_voice_channel(
                name=f'g{cntG}' ,category=after.channel.category
            )
            self.temp_channelsG.append(new_channel.id)
            await member.move_to(new_channel)
        # --- Game  ---

        # --- Game  ---
        for channel_id in self.temp_channelsG:
            channel = guild.get_channel(channel_id)
            if len(channel.members) == 0:
                await channel.delete()
                self.temp_channelsG.remove(channel_id)
                cntG -= 1
        # --- Game  ---


        # --- Chill ---
        for channel_id in self.temp_channelsC:
            channel = guild.get_channel(channel_id)
            if len(channel.members) == 0:
                await channel.delete()
                self.temp_channelsC.remove(channel_id)
                cntC -= 1
        # --- Chill ---