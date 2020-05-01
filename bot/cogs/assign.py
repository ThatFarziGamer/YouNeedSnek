import asyncio
import logging
from datetime import datetime

from discord.ext import commands


logger = logging.getLogger(__name__)


class Assign(commands.Cog):
    """A cog to assign specific roles."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="assign")
    async def assing_trusted_role(self, ctx):
        smp_role_id = 489176009120415744
        trusted_role_id = 705274433723564083
        guild = ctx.guild
        all_members = guild.members
        print(len(all_members))
        for member in all_members:
            member_join_date = member.joined_at
            today = datetime.now()
            days_present = today-member_join_date

            roles_id = [role.id for role in member.roles]
            if smp_role_id in roles_id:
                if days_present.days > 28:
                    trusted_role = guild.get_role(trusted_role_id)
                    await member.add_roles(trusted_role)
                    logger.info(f"{str(member)} is given the {trusted_role.name} role.")
                    await asyncio.sleep(1)
                else:
                    pass


def setup(bot):
    bot.add_cog(Assign(bot))
    logger.info("Assign Cog loaded.")
