import logging
import sys
import os
import yaml

import discord
from discord.ext import commands


logger = logging.getLogger(__name__)

with open("config.yml") as f:
    yaml_data = yaml.full_load(f)
token = yaml_data["bot"]["token"]
prefix = yaml_data["bot"]["prefix"]


class YNBBot(commands.Bot):
    """An instance of the bot."""

    def __init__(self):
        super().__init__(command_prefix="?",
                         description="YNB Bot.")

    async def on_ready(self):

        # list of all the cogs.
        cogs = [cog for cog in os.listdir("bot/cogs") if cog.endswith(".py")]

        for cog in cogs:
            try:
                # loading the cogs
                self.load_extension("bot.cogs." + os.path.splitext(cog)[0])

            except Exception as e:
                # in case any cog/s did not load.
                logger.error(f"Could not load extension {cog} due to error:\n{e}")
                sys.exit()

        logger.info(f'Running as {self.user.name} with ID: {self.user.id}')
        await self.change_presence(activity=discord.Game(name="You need bear!"))

    def run(self):
        # running the bot.
        with open("config.yml") as f:
            data = yaml.full_load(f)
            token = data["bot"]["token"]
        super().run(token, bot=True, reconnect=True)


if __name__ == "__main__":
    bot = YNBBot()
    bot.remove_command("help")
    bot.run()
