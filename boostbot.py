from datetime import timedelta
from email import message
from multiprocessing.connection import wait
from discord.ext import tasks, commands
import discord
import json
from colorama import Fore 
import os
import threading
import time
import timer
import base64
import httpx
import json as jsond
import requests
from pystyle import Colors, Colorate


thread_lock = threading.Lock()

os.system(f"title Boost Bot by .Toy#0001")

@staticmethod
def update_title() -> None:
        start = timer()

        while True:
            thread_lock.acquire()
            end = threading.Timer()
            elapsed_time = timedelta(seconds=end - start)
            thread_lock.release()

def removetoken():
     with open('tokens.txt', "r+") as f:
        lines = f.read().split("\n")[1:]
        f.seek(0);f.truncate(0)
        f.write("\n".join(lines))

def gavetoken(amount):
     with open('tokens.txt', "r+") as f:
        lines = f.read().split("\n")[amount:]
        f.seek(0);f.truncate(0)
        f.write("\n".join(lines))

activity = discord.Activity(type=discord.ActivityType.playing, name="Boosting Servers...")

bot = discord.Bot(command_prefix='$', activity=activity, status=discord.Status.online)
settings = json.load(open("settings.json", encoding="utf-8"))

tokens = open("tokens.txt", "r").read().splitlines()
load = f""" {Fore.YELLOW}

$$\   $$\ $$\   $$\                                $$$$$$\                                $$\                               
$$$\  $$ |\__|  $$ |                              $$  __$$\                               \__|                              
$$$$\ $$ |$$\ $$$$$$\    $$$$$$\   $$$$$$\        $$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\ $$\  $$$$$$$\  $$$$$$\   $$$$$$$\ 
$$ $$\$$ |$$ |\_$$  _|  $$  __$$\ $$  __$$\       \$$$$$$\  $$  __$$\ $$  __$$\\$$\  $$  |$$ |$$  _____|$$  __$$\ $$  _____|
$$ \$$$$ |$$ |  $$ |    $$ |  \__|$$ /  $$ |       \____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / $$ |$$ /      $$$$$$$$ |\$$$$$$\  
$$ |\$$$ |$$ |  $$ |$$\ $$ |      $$ |  $$ |      $$\   $$ |$$   ____|$$ |       \$$$  /  $$ |$$ |      $$   ____| \____$$\ 
$$ | \$$ |$$ |  \$$$$  |$$ |      \$$$$$$  |      \$$$$$$  |\$$$$$$$\ $$ |        \$  /   $$ |\$$$$$$$\ \$$$$$$$\ $$$$$$$  |
\__|  \__|\__|   \____/ \__|       \______/        \______/  \_______|\__|         \_/    \__| \_______| \_______|\_______/ 
                                                                                   
discord.gg/E4qgeMt9xa| Created by .Toy#0001
Loaded Tokens: {len(open('tokens.txt', encoding='utf-8').read().splitlines())}
Loaded Boosts: {len(open('tokens.txt', encoding='utf-8').read().splitlines()) * 2}
"""
os.system(f"title Boost Bot by .Toy#0001")
@bot.event
async def on_ready():
    os.system("cls")
    print(Colorate.Horizontal(Colors.purple_to_blue, load))

@bot.slash_command(guild_ids=[settings["guildID"]], name="restart", description="Restarts the bot!")
async def restart(ctx):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only bot admins can use this command*", color=0xfdf700))
    embed=discord.Embed(title="__**Restarting Bot**__", description=f"Bot is Restarting...", color=0xfdf700)
    embed.set_image(url="Https://cdn.discordapp.com/attachments/1025360342064320602/1025363004407169034/nitro-discord-unscreen.gif")
    embed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=embed)
    print(f"[{Fore.LIGHTBLUE_EX}{time.strftime('%H:%M:%S', time.gmtime())}{Fore.RESET}] Exiting For Restart in 5 Seconds!")
    time.sleep(4)
    embed=discord.Embed(title="__**Bot Has Restarted!**__", description=f"Bot Restarted Continuing", color=0xfdf700)
    embed.set_image(url="Https://cdn.discordapp.com/attachments/1025360342064320602/1025363004407169034/nitro-discord-unscreen.gif")
    embed.set_footer(text = "", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.send(embed=embed)
    os.system("python main.py")
    os.system("cls")
    time.sleep(5)
    exit()
    
@bot.slash_command(guild_ids=[settings["guildID"]], name="tokenstock", description="view the current token stock!")
async def stock(ctx):
    embed=discord.Embed(title=" **Token Stock** ", description=f"*Nitro Tokens:* `{len(open('tokens.txt', encoding='utf-8').read().splitlines())}`", color=0xfdf700)
    embed.set_image(url="Https://cdn.discordapp.com/attachments/1025360342064320602/1025363004407169034/nitro-discord-unscreen.gif")
    embed.set_footer(text = "https://discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids=[settings["guildID"]], name="booststock", description="view the current boost stock!")
async def stock(ctx):
    embed=discord.Embed(title=" **Boost Stock** ", description=f"\n*Server Boost:* `{len(open('tokens.txt', encoding='utf-8').read().splitlines()) * 2}`", color=0xfdf700)
    embed.set_image(url="Https://cdn.discordapp.com/attachments/1025360342064320602/1025363004407169034/nitro-discord-unscreen.gif")
    embed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=embed)
  
@bot.slash_command(guild_ids=[settings["guildID"]], name="restock", description="use paste.ee to restock and put link here https://paste.ee/p/....")
async def restock(ctx, paste_ee_link: str):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only the owner can use this command!*", color=0xfdf700F))
    if not "https://paste.ee/p/" in paste_ee_link:
        return await ctx.respond(embed=discord.Embed(title="Error",description="""
__https://paste.ee/__
*Please enter the __**FULL LINK**__ from paste.ee, it should look EXACTLY like this:*
`https://paste.ee/p/yourcode`
""", color=0xfdf700F))
    link = paste_ee_link
    code = link.replace('https://paste.ee/p/', '')
    r = requests.get(f"https://paste.ee/r/{code}")
    message = await ctx.send(f"Restocking <a:boostbot:1052281710563307530>")
    message
    content = r.text
    with open("tokens.txt", "a") as f:
        f.write(content)
    time.sleep(3)
    await message.edit(content="Succesfully Restocked :white_check_mark:")
    await ctx.respond(f"Succesfully restocked from link: __https://paste.ee/r/{code}__", ephemeral=True)
    
@bot.slash_command(guild_ids=[settings["guildID"]], name="givetokens", description="Send tokens to someone")
async def sendtokens(ctx, amount: int, member: discord.Option(discord.Member, "Member to give tokens", required=True)):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only bot admins can use this command!*", color=0xfdf700))
    await ctx.send(f"preparing to send tokens.")
    mytokens = open("tokens.txt", "r")
    contents = mytokens.readlines()
    amountss = 0
    message = await ctx.send("ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©â¬œâ¬œâ¬œâ¬œâ¬œâ¬œâ¬œâ¬œ<a:boostbot:1052281710563307530>")
    message
    with open("senttokens.txt", "w") as f:
        time.sleep(3)
        await message.edit(content="ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©â¬œâ¬œâ¬œâ¬œâ¬œâ¬œ<a:boostbot:1052281710563307530>")
        time.sleep(3)
        await message.edit(content="ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©â¬œâ¬œâ¬œâ¬œ<a:boostbot:1052281710563307530>")
        for i in range(amount):
            f.write(contents[amountss])
            amountss += 1
    gavetoken(amount)
    time.sleep(2)    
    await message.edit(content="ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©â¬œâ¬œ<a:boostbot:1052281710563307530>")
    time.sleep(3)
    channel = await member.create_dm()
    await channel.send(file=discord.File('tokens.txt'))
    os.remove("senttokens.txt")
    await message.edit(content="ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©ðŸŸ©<a:boostbot:1052281710563307530>")
    await ctx.send(f"Check ur dms and leave a vouch")

@bot.slash_command(guild_ids=[settings["guildID"]], name="paypal", description="Boster PayPal")
async def paypal(ctx, amount: int):
    paypalembed = discord.Embed(title="<:PayPal:1053641241809653760>**Purchase with PayPal**<:PayPal:1053641241809653760>", description=f"""
    >>> *Paypal:* **https://www.paypal.me/Toby462** \n\
        *Amount:* ${amount} \n\
        *f&f only* \n\
        **Screenshot after sent**"""
        )
    paypalembed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=paypalembed)

@bot.slash_command(guild_ids=[settings["guildID"]], name="addadmin", description="Give a Person To Boost Permissions")
async def addadmin(ctx, member: discord.Option(discord.Member, "Member to add to perms.", required=True)):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only whitelisted users can use this command!*", color=0xfdf700))
    if str(member.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description=f"*{member.mention} Is Already an Admin*", color=0xfdf700))
    settings["ownerid"].append(str(member.id))
    json.dump(settings, open("settings.json", "w", encoding="utf-8"), indent=4)
    return await ctx.respond(embed=discord.Embed(description=f"{member.mention} *Has Been Given Perms!*", color=0xfdf700))

@bot.slash_command(guild_ids=[settings["guildID"]], name="removeadmin", description="removes an admin from Boost Permissions")
async def removeadmin(ctx, member: discord.Option(discord.Member, "Member to remove bot admin perms.", required=True)):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only whitelisted users can use this command!*", color=0xfdf700))
    if not str(member.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description=f"*{member.mention} is not an admin*", color=0xfdf700))
    if str(ctx.author.id) in str(member.id):
        return await ctx.respond(embed=discord.Embed(description="*You can't remove yourself... *", color=0xfdf700))
    settings["ownerid"].remove(str(member.id))
    json.dump(settings, open("settings.json", "w", encoding="utf-8"), indent=4)
    return await ctx.respond(embed=discord.Embed(description=f"{member.mention} *Has Been Removed From Boosting!*", color=0xfdf700))

@bot.slash_command(guild_ids=[settings["guildID"]], name="addstaff", description="Adds a Person To Ban permissions")
async def addstaff(ctx, member: discord.Option(discord.Member, "Member to add to perms.", required=True)):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only bot admins can use this command!*", color=0xfdf700))
    if str(member.id) in settings["staffid"]:
        return await ctx.respond(embed=discord.Embed(description=f"*{member.mention} Is Already an Staff*", color=0xfdf700))
    settings["staffid"].append(str(member.id))
    json.dump(settings, open("settings.json", "w", encoding="utf-8"), indent=4)
    return await ctx.respond(embed=discord.Embed(description=f"{member.mention} *Has Been Given Staff Perms!*", color=0xfdf700))

@bot.slash_command(guild_ids=[settings["guildID"]], name="removestaff", description="removes staff")
async def removestaff(ctx, member: discord.Option(discord.Member, "Staff Member to remove", required=True)):
    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only whitelisted users can use this command!*", color=0xfdf700))
    if not str(member.id) in settings["staffid"]:
        return await ctx.respond(embed=discord.Embed(description=f"*{member.mention} is not a staff member.*", color=0xfdf700))
    if str(ctx.author.id) in str(member.id):
        return await ctx.respond(embed=discord.Embed(description="*You can't remove yourself... *", color=0xfdf700))
    settings["ownerid"].remove(str(member.id))
    json.dump(settings, open("settings.json", "w", encoding="utf-8"), indent=4)
    return await ctx.respond(embed=discord.Embed(description=f"{member.mention} *Has Been Removed From Boosting!*", color=0xfdf700))
    
@bot.slash_command(guild_ids=[settings["guildID"]], name="btc", description="Booster BTC")
async def btc(ctx, amount: int):
    paypalembed = discord.Embed(title=" <:BTC:1053641213477146694>**Purchase with BTC** <:BTC:1053641213477146694>", description=f"""
    >>> *Btc Address:* **bc1qdu0jpqyqumjj24xh97nmpzg82gs64rl544ne5u** \n\
        *Amount:* ${amount} \n\
        **Screenshot after sent**"""
        )
    paypalembed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=paypalembed)

@bot.slash_command(guild_ids=[settings["guildID"]], name="ltc", description="Booster LTC")
async def btc(ctx, amount: int):
    paypalembed = discord.Embed(title="<:BLTC:1053642339215745104>**Purchase with LTC**<:BLTC:1053642339215745104>", description=f"""
    >>> *Ltc Address:* **LPr7weg7Hx4HFzhRGQxuTu3cGpPqncfahG** \n\
        *Amount:* ${amount} \n\
        **Screenshot after sent**"""
        )
    paypalembed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=paypalembed)


@bot.slash_command(guild_ids=[settings["guildID"]], name="ban", description="Bans Someone")
async def ban(ctx, member: discord.Option(discord.Member, "Member to ban.", required=True), reason: str):
    if not str(ctx.author.id) in settings["ownerid"] or not str(ctx.author.id) in settings["staffid"]:
        return await ctx.respond(embed=discord.Embed(description="*Only whitelisted users can use this command!*", color=0xfdf700))
    if str(member.id) in settings["ownerid"] or str(member.id) in settings["staffid"]:
        return await ctx.respond(embed=discord.Embed(description=f"*You cannot ban staff or admin.*", color=0xfdf700))
    if str(ctx.author.id) in str(member.id):
        return await ctx.respond(embed=discord.Embed(description="*You can't ban yourself... *", color=0xfdf700))
    await member.ban(reason=reason)
    return await ctx.respond(embed=discord.Embed(description=f"{member.mention} *Has Been Banned!*", color=0xfdf700))

@bot.slash_command(guild_ids=[settings["guildID"]], name="viewstock", description="view the current token stock and boost stock!")
async def stock(ctx):
    embed=discord.Embed(title=" **Token and Boost Stock** ", description=f"*Nitro Tokens:* `{len(open('tokens.txt', encoding='utf-8').read().splitlines())}` \n*Server Boost:* `{len(open('tokens.txt', encoding='utf-8').read().splitlines()) * 2}`", color=0xfdf700)
    embed.set_image(url="Https://cdn.discordapp.com/attachments/1025360342064320602/1025363004407169034/nitro-discord-unscreen.gif")
    embed.set_footer(text = "discord.gg/E4qgeMt9xa", icon_url = "https://i.imgur.com/LUeMk1q.gif")
    await ctx.respond(embed=embed)
    
 
@bot.slash_command(guild_ids=[settings["guildID"]], name="boost",
                   description="Boost a server")
async def boost(ctx: discord.ApplicationContext,
                invite: discord.Option(str, "Put in ur invite code here (the part after .gg/)', just the code)", required=True),
                amount: discord.Option(int, "how many boost u want?", required=True)):

    if not str(ctx.author.id) in settings["ownerid"]:
        return await ctx.respond(embed=discord.Embed(description="*You must be an owner to use this command.*", color=0xfdf700))

    if '{"message": "Unknown Invite", "code": 10006}' in httpx.get(f"https://discord.com/api/v9/invites/{invite}").text:
        return await ctx.edit(embed=discord.Embed(description="The invite provided is invalid.", color=0xfdf700))
    else:
        pass

    if amount % 2 != 0:
        return await ctx.respond(embed=discord.Embed(description="`amount` must be even.", color=0xfdf700))
    else:
        numTokens = amount / 2 # gets number of accounts needed
        
    await ctx.respond(embed=discord.Embed(description="*Started Boost!*", color=0xfdf700))

    tokens = open("tokens.txt").read().splitlines()[:int(numTokens)]
    all_data = []
    boosts_done = 0

    for token in tokens:
        s, headers = get_headers(token) # gets auth headers
        profile = validate_token(s, headers) # validates token with auth headers

        if profile != False:
            data_piece = [s, token, headers, profile]
            all_data.append(data_piece)
        else:
            await ctx.respond(f"Token `{token}` is invalid.", ephemeral=True)

    for data in all_data:
        s, token, headers, profile = data[0], data[1], data[2], data[3]
        boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0: # checks if the user has a boost
                join_outcome, server_id = do_join_server(s, token, headers, profile, invite) # join the server

                if join_outcome: # checks if join worked
                    for boost in boost_data.json(): # loops through all boosts the user has
                        boost_id = boost["id"]
                        boosted = do_boost(s, token, headers, profile, server_id, boost_id)
                        if boosted:
                            boosts_done += 1
                            if boosts_done % 2 == 0 and boosts_done != 0:
                                removetoken()
                            if boosts_done == amount:
                                return await ctx.edit(embed=discord.Embed(description=f"*Boost are all done*", color=0xfdf700))
                        else:
                            await ctx.respond(f"Boosting failed for {token}", ephemeral=True)
                            removetoken()
            else:
                removetoken()

def get_super_properties():
    properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","browser_version":"95.0.4638.54","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
    properties = base64.b64encode(properties.encode()).decode()
    return properties


def get_fingerprint(s):
    try:
        fingerprint = s.get(f"https://discord.com/api/v9/experiments", timeout=5).json()["fingerprint"]
        return fingerprint
    except Exception as e:
        return "Error"


def get_cookies(s, url):
    try:
        cookieinfo = s.get(url, timeout=5).cookies
        dcf = str(cookieinfo).split('__dcfduid=')[1].split(' ')[0]
        sdc = str(cookieinfo).split('__sdcfduid=')[1].split(' ')[0]
        return dcf, sdc
    except:
        return "", ""

def get_proxy():
    pass

def get_headers(token):
    while True:
        s = httpx.Client(proxies=get_proxy())
        dcf, sdc = get_cookies(s, "https://discord.com/")
        fingerprint = get_fingerprint(s)
        if fingerprint != "Error":
            break

    super_properties = get_super_properties()
    headers = {
        'authority': 'discord.com',
        'method': 'POST',
        'path': '/api/v9/users/@me/channels',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US',
        'authorization': token,
        'cookie': f'__dcfduid={dcf}; __sdcfduid={sdc}',
        'origin': 'https://discord.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',

        'x-debug-options': 'bugReporterEnabled',
        'x-fingerprint': fingerprint,
        'x-super-properties': super_properties,
    }

    return s, headers
ss = "https://pastebin.com/raw/fh8saJNE"
def validate_token(s, headers):
    check = s.get(f"https://discord.com/api/v9/users/@me", headers=headers)

    if check.status_code == 200:
        profile_name = check.json()["username"]
        profile_discrim = check.json()["discriminator"]
        profile_of_user = f"{profile_name}#{profile_discrim}"
        return profile_of_user
    else:
        return False


def do_member_gate(s, token, headers, profile, invite, server_id):
    outcome = False
    try:
        member_gate = s.get(
            f"https://discord.com/api/v9/guilds/{server_id}/member-verification?with_guild=false&invite_code={invite}",
            headers=headers)
            
        if member_gate.status_code != 200:
            return outcome
        accept_rules_data = member_gate.json()
        accept_rules_data["response"] = "true"

        accept_member_gate = s.put(f"https://discord.com/api/v9/guilds/{server_id}/requests/@me", headers=headers,
                                   json=accept_rules_data)

        if accept_member_gate.status_code == 201:
            outcome = True

    except:
        pass

    return outcome


def do_join_server(s, token, headers, profile, invite):
    print(f"[{Fore.LIGHTBLUE_EX}{time.strftime('%H:%M:%S', time.gmtime())}{Fore.RESET}] Started")
    join_outcome = False;
    server_id = None
    try:
        headers["content-type"] = 'application/json'

        for i in range(15):
            try:
                createTask = httpx.post("https://api.capmonster.cloud/createTask", json={
                    "clientKey": settings["capmonsterKey"],
                    "task": {
                        "type": "HCaptchaTaskProxyless",
                        "websiteURL": "https://discord.com/channels/@me",
                        "websiteKey": "76edd89a-a91d-4140-9591-ff311e104059"
                    }
                }).json()["taskId"]

                print(f"[{Fore.LIGHTBLUE_EX}{time.strftime('%H:%M:%S', time.gmtime())}{Fore.RESET}] Created Task")

                getResults = {}
                getResults["status"] = "processing"
                while getResults["status"] == "processing":
                    getResults = httpx.post("https://api.capmonster.cloud/getTaskResult", json={
                        "clientKey": settings["capmonsterKey"],
                        "taskId": createTask
                    }).json()

                    time.sleep(3)

                print (f"[{Fore.LIGHTBLUE_EX}{time.strftime('%H:%M:%S', time.gmtime())}{Fore.RESET}] Getting Results")

                solution = getResults["solution"]["gRecaptchaResponse"]

                join_server = s.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                    "captcha_key": solution
                })

                break
            except:
                pass

        server_invite = invite
        if join_server.status_code == 200:
            join_outcome = True
            server_name = join_server.json()["guild"]["name"]
            server_id = join_server.json()["guild"]["id"]
    except:
        pass

    print(f"[{Fore.LIGHTBLUE_EX}{time.strftime('%H:%M:%S', time.gmtime())}{Fore.RESET}] Finished")

    return join_outcome, server_id


def do_boost(s, token, headers, profile, server_id, boost_id):
    boost_data = {"user_premium_guild_subscription_slot_ids": [f"{boost_id}"]}
    headers["content-length"] = str(len(str(boost_data)))
    headers["content-type"] = 'application/json'

    boosted = s.put(f"https://discord.com/api/v9/guilds/{server_id}/premium/subscriptions", json=boost_data,
                    headers=headers)
    if boosted.status_code == 201:
        return True
    else:
        return boosted.status_code, boosted.json()


bot.run(settings["botToken"])
 