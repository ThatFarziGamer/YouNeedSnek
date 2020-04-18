import discord
from discord.ext import commands
import time
import asyncio

rolename = []
MSG = []
LOG = []
roles = []
WEL = []
SM = []
SM1 = []
reactions = []

client = commands.Bot(command_prefix="?")
client.remove_command("help")


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Python"))
    guild_id = client.guilds[0].id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    channel = await guild.create_voice_channel("Time")
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

with open("YouNeedSnek.txt", "r") as f:
    file = f.readlines()

if file:
    try:
        R = file[0][:-1].split("||")
        for r in R:
            reactions.append(r.decode("utf-8"))
    except IndexError:
        reactions = []
    try:
        rolename = file[1][:-1].split("||")
        roles = file[2][:-1].split("||")
        Log = file[3][:-1].split("||")
        for i in range(len(Log)):
            LOg = Log[i].split()
            while "" in LOg:
                LOg.remove("")
            LOG.append(LOg)
        WEL = file[4][:-1].split("||")
        MSG = file[5][:-1].split("||")
        SM = file[6][:-1].split("||")
        SM1 = file[7][:-1].split("||")
    except IndexError:
        rolename, roles, LOG, WEL, MSG, SM, SM1 = [], [], [], [], [], [], []
        file = ["", "", "", "", "", "", "", ""]
else:
    file = ["", "", "", "", "", "", "", ""]


@client.command()  # only roles so far, add branches
@commands.has_permissions(manage_roles=True)
async def help(ctx, *, sentence):
    S = sentence.split()
    S = S[0].lower()
    if S == "branch":
        embed = discord.Embed(title="Branch Module", description="?branch <branch nick> <branch name> / ?branch <show>")
        embed.add_field(name="<branch name>", value="Specify the branch name as per the branch name on the YNB Discord.\nExample: The branch name for Survival Minecraft would be Survival Minecraft.", inline=False)
        embed.add_field(name="<branch nick>",
                        value="Define a shortened name for the specified branch.\nExample: smc as <branch nick> for the Survival Minecraft branch.",
                        inline=False)
        embed.add_field(name="<show>", value="Displays the currently integrated <branch names> & their <branch nicks>.", inline=False)
        embed.add_field(name="Editing:",
                        value="Re-run ?branch <branch nick> <branch name> with the updated changes to apply them. To delete the entry of a branch, re-run the command but leave the <branch name> empty.",
                        inline=False)
        await ctx.send(embed=embed)
    elif S == "record":
        embed = discord.Embed(title="Record Module", description="?record <branch nick> <add/remove> <Channel ID>\n?record <branch nick> <show>\n?record <show>")
        embed.add_field(name="<branch nick>",
                        value="Define a shortened name for the specified branch.\nExample: smc as <branch nick> for the Survival Minecraft branch.",
                        inline=False)
        embed.add_field(name="<show>", value="Displays the currently integrated <branch names> & their <branch nicks>.",
                        inline=False)
        embed.add_field(name="<add/remove>",
                        value="Use this to add/remove channel(s) from mentioned branch by mentioning them. Not mentioning them while using remove will clear the list of channels.",
                        inline=False)
        embed.add_field(name="<Channel ID>",
                        value="Channel ID in any form except name in plain text. For multiple channels, seperate them with a space bar and nothing else.",
                        inline=False)
        await ctx.send(embed=embed)
    elif S == "welcome":
        embed = discord.Embed(title="Welcome Module", description="?welcome <role nick> <#channel> <Message>")
        embed.add_field(name="<role nick>", value="Place in the short form or nick name for the branch.", inline=False)
        embed.add_field(name="<Channel ID>", value="Channel ID in any form except name in plain text.", inline=False)
        embed.add_field(name="<Message>",
                        value="Similar to ?message, just for special commands required for whitelisting and stuff to be sent",
                        inline=False)
        embed.add_field(name="Editing", value="Re run the code with required changes. Only editable. Can't be deleted.", inline=False)
        await ctx.send(embed=embed)
    elif S == "command":
        embed = discord.Embed(title="Command Module", description="?command <role nick> <Channel ID> <Command>")
        embed.add_field(name="<role nick>", value="Place in the short form or nick name for the branch.", inline=False)
        embed.add_field(name="<Channel ID>", value="Channel ID in any form except name in plain text.", inline=False)
        embed.add_field(name="<Command>",
                        value="Similar to ?message, just for special commands required for whitelisting and stuff to be sent",
                        inline=False)
        await ctx.send(embed=embed)
    elif S == "recruit":
        embed = discord.Embed(title="Recruit Module", description="?recruit <Player ID> <In-game Name> <role nick> <Age> <Notes>")
        embed.add_field(name="<Player ID>", value="Player's Discord ID", inline = False)
        embed.add_field(name="<In-Game ID>", value="Player's Username.", inline=False)
        embed.add_field(name="<branch nick>",
                        value="Define a shortened name for the specified branch.\nExample: smc as <branch nick> for the Survival Minecraft branch.",
                        inline=False)
        embed.add_field(name="<Age>", value="Player's age.", inline=False)
        embed.add_field(name="<Notes>", value="Additional notes about the player.", inline=False)
        await ctx.send(embed=embed)
    elif S == "all":
        embed = discord.Embed(title="Help Overview")
        embed.add_field(name="branch",
                        value="This command handles branches.\nUse ?help branch for a complete guide.",
                        inline=False)
        embed.add_field(name="record",
                        value="This command handles branch specific channels records on members.\nUse ?help record for a complete guide.",
                        inline=False)
        embed.add_field(name="welcome",
                        value="This command handles branch specific welcome channels.\nUse ?help welcome for a complete guide.",
                        inline=False)
        embed.add_field(name="command",
                        value="This command handles branch specific commands and their channels.\nUse ?help command for a complete guide.",
                        inline=False)
        embed.add_field(name="recruit",
                        value="This command handles branch wise recruitment.\nUse ?help recruit for a complete guide.",
                        inline=False)
        await ctx.send(embed=embed)


@client.command()  # only roles so far, add branches
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

@client.command()  # Replaces botlog
@commands.has_permissions(manage_roles=True)
async def record(ctx, *, sentence):
    S = sentence.split(" ")
    if S[0].lower() == "show":
        embed = discord.Embed(title="Roles and Channels", color=0x000000)
        for i in range(len(rolename)):
            b = ""
            if LOG[i]:
                for j in range(len(LOG[i])):
                    b = b + "<#" + str(LOG[i][j]) + ">"
                    if j == len(LOG[i]) - 1:
                        b = b + "."
                    else:
                        b = b + ", "
            else:
                b = "None yet!"
            embed.add_field(name=rolename[i], value=b, inline=False)
        await ctx.send(embed=embed)
    else:
        for i in range(len(roles)):
            if S[0].lower() == rolename[i] and S[1].lower() == "add":
                for j in range(2, len(S)):
                    if S[j][0] == "<":
                        S[j] = S[j][2:-1]
                    if S[j] not in LOG[i]:
                        LOG[i].append(S[j])
                    print(LOG)
                    print(await client.fetch_channel(S[j]))
            elif S[0].lower() == rolename[i] and S[1].lower() == "remove":
                if len(S) == 2:
                    LOG[i] = []
                else:
                    for j in range(2, len(S)):
                        if S[j][0] == "<":
                            S[j] = S[j][2:-1]
                        if S[j] in LOG[i]:
                            LOG[i].remove(S[j])
            elif S[0].lower() == rolename[i]:
                b = ""
                embed = discord.Embed(title="Roles and Channels", color=0x000000)
                if LOG[i]:
                    for j in range(len(LOG[i])):
                        print(LOG[i][j], type(LOG[i][j]))
                        b = b + "<#" + str(LOG[i][j]) + ">"
                        if j == len(LOG[i]) - 1:
                            b = b + "."
                        else:
                            b = b + ", "
                else:
                    b = "None yet!"
                embed.add_field(name=rolename[i], value=b, inline=False)
                await ctx.send(embed=embed)
        log = ""
        for i in range(len(LOG)):
            for j in range(len(LOG[i])):
                log = log + LOG[i][j]
                if j != len(LOG[i]) - 1:
                    log = log + "|"
            if i != len(LOG) - 1:
                log = log + "||"
        file[3] = log + "\n"
        print(file)
        with open("YouNeedSnek.txt", "w") as f:
            f.writelines(file)
            

@client.command()  # only roles so far, add branches
@commands.has_permissions(manage_roles=True)
async def branch(ctx, *, sentence):
    S = sentence.split(" ")
    nn = S[0].lower()
    if nn == "show":
        embed = discord.Embed(title="Nickname of Roles", color=0x000000)
        for i in range(len(roles)):
            embed.add_field(name=roles[i], value=rolename[i], inline=False)
        await ctx.send(embed=embed)
    elif len(S) > 1:
        rn = ""
        for i in range(1, len(S)):
            rn = rn + S[i]
            if i != len(S) - 1:
                rn = rn + " "
        if rn not in roles and nn not in rolename:
            roles.append(rn)  # official_names
            rolename.append(nn)  # Nick of roles
            WEL.append([])
            LOG.append([])
            MSG.append("None")
            SM.append("")
            SM1.append("")
        elif rn in roles and nn not in rolename:
            for i in range(len(roles)):
                if rn == roles[i]:
                    rolename[i] = nn
                    
        elif rn not in roles and nn in rolename:
            for i in range(len(rolename)):
                if nn == rolename[i]:
                    roles[i] = rn
    else:
        for i in range(len(rolename)):
            if nn == rolename[i]:
                roles.pop(i)
                rolename.pop(i)
                WEL.pop(i)
                LOG.pop(i)
                MSG.pop(i)
                SM.pop(i)
                SM1.pop(i)
    log = ""
    for i in range(len(rolename)):
        log = log + rolename[i]
        if i != len(rolename) - 1:
            log = log + "||"
    file[1] = log + "\n"
    log = ""
    for i in range(len(roles)):
        log = log + roles[i]
        if i != len(roles) - 1:
            log = log + "||"
    file[2] = log + "\n"
    log = ""
    for i in range(len(LOG)):
        for j in range(len(LOG[i])):
            log = log + LOG[i][j]
            if j != len(LOG[i])-1:
                log = log + "|"
        if i != len(LOG) - 1:
            log = log + "||"
    file[3] = log + "\n"
    log = ""
    for i in range(len(WEL)):
        log = log + WEL[i]
        if i != len(WEL) - 1:
            log = log + "||"
    file[4] = log + "\n"
    log = ""
    for i in range(len(MSG)):
        log = log + MSG[i]
        if i != len(MSG) - 1:
            log = log + "||"
    file[5] = log + "\n"
    log = ""
    for i in range(len(SM)):
        log = log + SM[i]
        if i != len(SM) - 1:
            log = log + "||"
    file[6] = log + "\n"
    log = ""
    for i in range(len(SM1)):
        log = log + SM1[i]
        if i != len(SM1) - 1:
            log = log + "||"
    file[7] = log + "\n"
    with open("YouNeedSnek.txt", "w") as f:
        f.writelines(file)
    print(LOG, WEL)


@client.command()
@commands.has_permissions(manage_roles=True)
async def welcome(ctx, *, sentence):
    S = sentence.split(" ")
    if S[0].lower() == "show":
        embed = discord.Embed(title="Roles, Channels and Messages", color=0x000000)
        for i in range(len(rolename)):
            b = ""
            if WEL[i]:
                b = b + "<#" + str(WEL[i]) + ">"
            else:
                b = "None yet!"
            b = b + "\n" + MSG[i]
            embed.add_field(name=roles[i], value=b, inline=False)
        await ctx.send(embed=embed)
    else:
        for i in range(len(rolename)):
            if S[0].lower() == rolename[i]:
                msg = ""
                if S[1][0] == "<":
                    S[1] = S[1][2:-1]
                for j in range(2, len(S)):
                    msg = msg + S[j]
                    if j != len(S) - 1:
                        msg = msg + " "
                WEL[i] = S[1]
                MSG[i] = msg
                log = ""
                for k in range(len(WEL)):
                    log = log + WEL[k]
                    if k != len(WEL) - 1:
                        log = log + "||"
                file[4] = log + "\n"
                log = ""
                for k in range(len(MSG)):
                    log = log + MSG[k]
                    if k != len(MSG) - 1:
                        log = log + "||"
                file[5] = log + "\n"
                with open("YouNeedSnek.txt", "w") as f:
                    f.writelines(file)


@client.command()
@commands.has_permissions(manage_roles=True)
async def recruit(ctx, *, sentence):
    authorc = ctx.author
    print(authorc.roles)
    print([y.id for y in authorc.roles])
    if 516208259099525134 in [y.id for y in authorc.roles] and str(ctx.channel) == "chat-and-commands":
        notes = ""
        L = str(sentence).split(" ")
        while L[2] not in rolename:
            L[1] += " " + L[2]
            L.pop(2)
        for i in range(len(L) - 4):
            notes = notes + L[4 + i]
            if i != len(L) - 5:
                notes = notes + " "
        player = str(await client.fetch_user(L[0][3:-1]))
        guild_id = client.guilds[0].id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m: m.name == player[:-5], guild.members)
        print(ctx.channel)
        print(member.roles)
        if 667036535476191232 in [y.id for y in member.roles]:
            print("Cleared qualifications")
            for i in range(len(roles)):
                if rolename[i] == L[2].lower():
                    tag = roles[i]
            role = discord.utils.get(guild.roles, name=tag)
            await member.add_roles(role)
            await member.edit(nick=L[1])
            embed = discord.Embed(title="New Member Details",
                                  color=0x000000)
            embed.add_field(name="Discord ID", value=L[0], inline=True)
            embed.add_field(name="In-game ID", value=L[1], inline=True)
            embed.add_field(name="Branch", value=role, inline=True)
            embed.add_field(name="Age", value=L[3], inline=True)
            embed.add_field(name="Notes", value=notes, inline=True)
            await ctx.send(embed=embed)
            print(ctx.channel, id)
            for j in range(len(roles)):
                if tag == roles[j]:
                    for i in LOG[j]:
                        if i != ctx.channel.id:
                            channel = await client.fetch_channel(i)
                            await channel.send(embed=embed)
                    wel = MSG[j]
                    W = wel.split(" ")
                    wel = ""
                    for i in range(len(W)):
                        if W[i] == "player":
                            W[i] = L[0]
                        wel = wel + W[i]
                        if i != len(W) - 1:
                            wel = wel + " "
                    for i in WEL[j]:
                        channel = await client.fetch_channel(i)
                        await channel.send(f"{wel}")
                    W=SM1[j].split()
                    wel=""
                    for i in range(len(W)):
                        if W[i] == "player":
                            W[i] = L[1]
                        wel = wel + W[i]
                        if i != len(W) - 1:
                            wel = wel + " "
                    channel = await client.fetch_channel(SM[j])
                    await channel.send(f"{wel}")

            print("Success")
        else:
            await ctx.send(
                f"Conditions not met! {L[0]} lacks the Social Role. When the said role is present please rerun the command.")


@client.event
async def on_message(message):
    if str(message.channel) == "feedback":
        for i in reactions:
            await message.add_reaction(i)
    await client.process_commands(message)


client.run("BOT_TOKEN")