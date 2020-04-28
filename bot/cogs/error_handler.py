import logging

from discord.ext import commands


log = logging.getLogger('bot.' + __name__)


class ErrorHandler(commands.Cog):
    """Cog to handle errors."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Fires when a command throws an error."""
        if isinstance(error, commands.UserInputError):
            log.debug(f'{ctx.author} used {ctx.command} but invalid arguments were passed.')
            await ctx.send(f"Invalid arguments! please try again.\n{error}")

        else:
            raise error


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
    log.debug("Loaded")
