import logging
from pathlib import Path

import discord
from discord.ext import commands


logger = logging.getLogger(__name__)


class Feedback(commands.Cog):
    """A cog to handle feedback channel reactions"""
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="reaction")
    async def reaction(self, ctx):
        """Handles reactions relating to the feedback channel."""
        pass

    @reaction.command(name="add", aliases=["append", "xyz"])
    async def add_reaction(self, ctx, emoji_name: str):
        """Store emoji ID in a text file"""
        all_emojis = ctx.guild.emojis
        emoji_id = 0
        for emoji in all_emojis:
            if emoji.name == emoji_name:
                emoji_id = emoji.id
                break

        path_of_file = Path("YouNeedSnek.txt")
        with path_of_file.open(mode="a") as f:
            f.write(f"{emoji_id}\n")
        await ctx.send("Emoji has been added!")

    @reaction.command(name="show")
    async def show_reaction(self, ctx):
        path_of_file = Path("YouNeedSnek.txt")
        all_emojis = path_of_file.read_text()
        if not all_emojis:
            return await ctx.send("No emojis available.")
        embed = discord.Embed(color=discord.Colour.blue())
        embed.title = "Feedback Reaction Emojis"
        embed.description = all_emojis
        await ctx.send(embed=embed)

    @reaction.command(name="remove")
    async def remove_reaction(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Feedback(bot))
    logger.info("Feedback cog loaded.")
