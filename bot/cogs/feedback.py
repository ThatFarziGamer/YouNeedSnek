import logging


from discord.ext import commands


logger = logging.getLogger(__name__)


class Feedback(commands.Cog):
    """Commands relating to feedback channel."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # only roles so far, add branches
    @commands.has_permissions(manage_roles=True)
    async def reaction(ctx, *, sentence):
        S = sentence.split(" ")
        if S[0].lower() == "add":
            for i in S[1:]:
                if i.encode("utf-8") not in reactions:
                    reactions.append(i.encode("utf-8"))
        elif S[0].lower() == "remove":
            for i in S[1:]:
                if i.encode("utf-8") in reactions:
                    reactions.remove(i.encode("utf-8"))
        elif S[0].lower() == "show":
            r = ""
            for i in reactions:
                r = r + i.decode("utf-8")
                if i == reactions[-1]:
                    r = r + "."
                else:
                    r = r + ", "
            embed = discord.Embed(title="Reactions", description=r)
            await ctx.send(embed=embed)
            print(reactions)
        r = ""
        for i in range(len(reactions)):
            r = r + str(reactions[i])
            if i != len(reactions) - 1:
                r = r + "||"
        file[0] = r + "\n"
        with open("YouNeedSnek.txt", "w") as f:
            f.writelines(file)


def setup(bot):
    bot.add_cog(Feedback(bot))
    logger.info("Recruitment cog loaded.")