import asyncio
import logging
import time

import discord
import yaml
from discord.ext import commands


logger = logging.getLogger(__name__)
with open("config.yml") as f:
    yaml_data = yaml.full_load(f)
guild_id = yaml_data["guild"]["id"]



class VoiceClock(commands.Cog):
    """Handle voice channel that displays time in UTC."""
    def __init__(self, bot):
        self.bot = bot

    async def config_clock(self):
        guild = self.bot.get_guild(int(guild_id))
        channel_dict = {}
        voice_channels = guild.voice_channels  # a list


        channel_id = None
        for channel in voice_channels:
            if "UTC" in channel.name:
                channel_id = channel.id

        if not channel_id:
            channel = await guild.create_voice_channel("Time")
        else:
            channel = guild.get_channel(channel_id)

        await channel.set_permissions(guild.default_role, connect=False)
        while 1 != 2:
            t = time.gmtime(time.time())
            if len(str(t[4])) == 1:
                b = "0" + str(t[4])
            else:
                b = str(t[4])
            if len(str(t[3])) == 1:
                a = "0" + str(t[3])
            else:
                a = str(t[3])
            if a in ["23", "11"] and int(b) >= 45 or a in ["12", "00"] and int(b) < 15:
                cl = "🕛"
            elif a in ["12", "00"] and int(b) >= 15 and int(b) < 45:
                cl = "🕧"
            elif a in ["12", "00"] and int(b) >= 45 or a in ["13", "01"] and int(b) < 15:
                cl = "🕐"
            elif a in ["13", "01"] and int(b) >= 15 and int(b) < 45:
                cl = "🕜"
            elif a in ["13", "01"] and int(b) >= 45 or a in ["14", "02"] and int(b) < 15:
                cl = "🕑"
            elif a in ["14", "02"] and int(b) >= 15 and int(b) < 45:
                cl = "🕝"
            elif a in ["14", "02"] and int(b) >= 45 or a in ["15", "03"] and int(b) < 15:
                cl = "🕒"
            elif a in ["15", "03"] and int(b) >= 15 and int(b) < 45:
                cl = "🕞"
            elif a in ["15", "03"] and int(b) >= 45 or a in ["16", "04"] and int(b) < 15:
                cl = "🕓"
            elif a in ["16", "04"] and int(b) >= 15 and int(b) < 45:
                cl = "🕟"
            elif a in ["16", "04"] and int(b) >= 45 or a in ["17", "05"] and int(b) < 15:
                cl = "🕔"
            elif a in ["17", "05"] and int(b) >= 15 and int(b) < 45:
                cl = "🕠"
            elif a in ["17", "05"] and int(b) >= 45 or a in ["18", "06"] and int(b) < 15:
                cl = "🕕"
            elif a in ["18", "06"] and int(b) >= 15 and int(b) < 45:
                cl = "🕡"
            elif a in ["18", "06"] and int(b) >= 45 or a in ["19", "07"] and int(b) < 15:
                cl = "🕖"
            elif a in ["19", "07"] and int(b) >= 15 and int(b) < 45:
                cl = "🕢"
            elif a in ["19", "07"] and int(b) >= 45 or a in ["20", "08"] and int(b) < 15:
                cl = "🕗"
            elif a in ["20", "08"] and int(b) >= 15 and int(b) < 45:
                cl = "🕣"
            elif a in ["20", "08"] and int(b) >= 45 or a in ["21", "09"] and int(b) < 15:
                cl = "🕘"
            elif a in ["21", "09"] and int(b) >= 15 and int(b) < 45:
                cl = "🕤"
            elif a in ["21", "09"] and int(b) >= 45 or a in ["22", "10"] and int(b) < 15:
                cl = "🕙"
            elif a in ["22", "10"] and int(b) >= 15 and int(b) < 45:
                cl = "🕥"
            elif a in ["22", "10"] and int(b) >= 45 or a in ["23", "11"] and int(b) < 15:
                cl = "🕚"
            elif a in ["23", "11"] and int(b) >= 15 and int(b) < 45:
                cl = "🕦"
            await discord.VoiceChannel.edit(channel, name=f"{cl} {a}:{b} UTC")
            await asyncio.sleep(5)


def setup(bot):
    bot.add_cog(VoiceClock(bot))
    loop = asyncio.get_event_loop()
    loop.create_task(VoiceClock(bot).config_clock())
    logger.info("VoiceClock cog loaded.")