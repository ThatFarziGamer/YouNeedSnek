import logging
import datetime
import os
import sys
import yaml
from pathlib import Path

import discord
from discord.ext import commands


def setup_logger() -> logging.Logger:
    """Create and return the root Logger object for the bot."""
    LOGDIR = Path('logs')
    LOGDIR.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    logfile = LOGDIR / f'{timestamp}.log'
    logger = logging.getLogger('bot')  # the actual logger instance
    logger.setLevel(logging.DEBUG)  # capture all log levels
    console_log = logging.StreamHandler()
    console_log.setLevel(logging.DEBUG)  # log levels to be shown at the console
    file_log = logging.FileHandler(logfile)
    file_log.setLevel(logging.DEBUG)  # log levels to be written to file
    formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}', style='{')
    console_log.setFormatter(formatter)
    file_log.setFormatter(formatter)
    logger.addHandler(console_log)
    logger.addHandler(file_log)
    # additionally, do some of the same configuration for the discord.py logger
    logging.getLogger('discord').setLevel(logging.ERROR)
    logging.getLogger('aiosqlite').setLevel(logging.ERROR)
    logging.getLogger('websockets').setLevel(logging.ERROR)
    return logger


logger = setup_logger()

with open("config.yml") as f:
    yaml_data = yaml.full_load(f)
token = yaml_data["bot"]["token"]
prefix = yaml_data["bot"]["prefix"]


class YNBBot(commands.Bot):
    """An instance of the bot."""

    def __init__(self):
        super().__init__(command_prefix=prefix,
                         description="YNB Bot.")

    async def on_ready(self):

        # list of all the cogs.
        cogs = [cog for cog in os.listdir("bot/cogs") if cog.endswith(".py")]

        for cog in cogs:

            self.load_extension("bot.cogs." + os.path.splitext(cog)[0])

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
    # bot.remove_command("help")
    bot.run()
