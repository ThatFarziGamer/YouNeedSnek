import logging
import re

import discord
from discord.ext import commands
from discord.ext.commands import EmojiConverter


logger = logging.getLogger(__name__)


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel) == "feedback":
            with open("YouNeedSnek.txt", "r") as f:
                emoji_ids = f.readlines()
                for emoji_id in emoji_ids:
                    emoji = self.bot.get_emoji(int(emoji_id))
                    await message.add_reaction(emoji)


def setup(bot):
    bot.add_cog(Events(bot))
    logger.info("Events cog loaded.")
