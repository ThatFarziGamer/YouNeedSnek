import logging

from discord.ext import commands


logger = logging.getLogger(__name__)

NEUTRAL_FACE_EMOJI = "😐"


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel) == "feedback":
            with open("YouNeedSnek.txt", "r") as f:
                emoji_ids = f.readlines()
            emoji_list = []
            for emoji_id in emoji_ids:
                emoji = self.bot.get_emoji(int(emoji_id))
                emoji_list.append(emoji)
            no_of_custom_emojis = len(emoji_list)
            emoji_list.insert(no_of_custom_emojis//2, NEUTRAL_FACE_EMOJI)

            for emoji in emoji_list:
                await message.add_reaction(emoji)


def setup(bot):
    bot.add_cog(Events(bot))
    logger.info("Events cog loaded.")
