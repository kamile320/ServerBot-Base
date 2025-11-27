import subprocess
import os

ver = "1.9.3-base"
displayname='ServerBot'
extendedErrMess = False

def os_selector():
    print(f"====ServerBot v{ver} Recovery Menu====")
    print("""Select Method: 
1 - Linux
2 - Windows
3 - Setup.sh
4 - Exit
""")
    sel = int(input('>>> '))
    if sel == 1:
        subprocess.run(['bash', 'Files/setup/setuplib.sh'])
    elif sel == 2:
        subprocess.run(['setup.bat'], shell=True)
    elif sel == 3:
        subprocess.run(['bash', 'setup.sh'])
    elif sel == 4:
        exit()
    else:
        print('Failed to run Script. Aborting Install...')
        exit()



try:
    import discord
    from discord.ext import commands
    from discord import *
    import datetime
    import psutil
    import asyncio
    import random
    import pyfiglet
    import platform
    from dotenv import load_dotenv
except Exception as exc:
    print(f"Error in importing Library's. Trying to install it and update pip3\nException: {exc}\n")
    os_selector()



#Baner
banner = pyfiglet.figlet_format(displayname)
bluescreenface = pyfiglet.figlet_format(": (")
print(banner)



#Intents
intents = discord.Intents.default()
intents.message_content = True
status = [f'{platform.system()} {platform.release()}', f'ServerBot v{ver}', displayname]
choice = random.choice(status)
client = commands.Bot(command_prefix='.', intents=intents, activity=discord.Game(name=choice))
testbot_cpu_type = platform.processor() or 'Unknown'
accept_value = ['True', 'true', 'Enabled', 'enabled', '1', 'yes', 'Yes', 'YES', True]



try:
    load_dotenv()
    ############# token/intents/etc ################
    admin_usr = os.getenv('admin_usr')
    mod_usr = os.getenv('mod_usr')
    ################################################
except:
    print("CAN'T LOAD .env FILE!\nCreate .env file using setup.sh")



#Log_File
logs = open('Logs.txt', 'w')
def createlogs():
    logs.write(f"""S E R V E R  B O T
LOGS
Time: {datetime.datetime.now()}
Info: Remember to shut down bot by .ShutDown command or log will be empty.
=============================================================================\n\n""")
    logs.close()
createlogs()

#LogMessage
def logMessage(info):
    time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    logs = open(f'{maindir}/Logs.txt', 'a', encoding='utf-8')
    logs.write(f'[{time}] {info}\n')
    logs.close()
#PrintMessage
def printMessage(info):
    time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(f'[{time}] {info}')


#Directory
maindir = os.getcwd()
SBbytes = os.path.getsize('ServerBot.py')


#Information/Errors
not_allowed = "You're not allowed to use this command."
random_err = 'Something went wrong. Have you typed correct min/max values?'


#MessageLogging
def channelLog(usr, usrmsg, chnl, srv, usr_id, chnl_id, srv_id):
    print(f"[Message//{srv}/{chnl}] {usr}: {usrmsg}")


#ClientEvent
@client.event
async def on_ready():
    print(f'Logged as {client.user}')
    print(f'Welcome in ServerBot v{ver}')
    #slash_command_sync
    try:
        syncd = await client.tree.sync()
        print(f'Synced {len(syncd)} slash command(s)')
    except:
        print("Can't sync slash commands")
    print('Bot runtime: ', datetime.datetime.now())
    print('=' *40)



@client.event
async def on_message(message):
    #Username
    username = str(message.author).split('#')[0]
    #UserMessage
    user_message = str(message.content)
    #Channel
    try:
        channel = str(message.channel.name)
    except AttributeError:
        channel = str(message.channel)
    #Server
    try:
        server = str(message.guild.name)
    except AttributeError:
        server = str(message.guild)
    #UserID
    userid = message.author.id
    #ChannelID
    channelid = message.channel.id
    #ServerID
    try:
        serverid = message.guild.id
    except AttributeError:
        serverid = "DM"

    channelLog(username, user_message, channel, server, userid, channelid, serverid)

    await client.process_commands(message)



        #ChatBot
#Chat
#1
# Default command scheme
@client.command(name='hello', help='Default command')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

#2
# Default command scheme made only for Admins
@client.command(name='hello_admin', help='Default command scheme made only for Admins')
async def hello_admin(ctx):
    if str(ctx.message.author.id) in admin_usr:
        await ctx.send(f'Hello Admin, {ctx.author.mention}!')
    else:
        await ctx.send(not_allowed)
        #ChatBot-END



        #Other Essential Commands
#1
@client.command(name='credits', help='Shows Credits')
async def credits(ctx):
    await ctx.send(f"""
***S e r v e r  B o t***
Version: {ver}
Created By: *Kamile320*.

Thanks to:
- friends for testing Bot
- <@632682413776175107> for some retranslations

Source: ```https://github.com/kamile320/ServerBot-Base```
Discord Server: [Here](https://discord.gg/UMtYGAx5ac)
""")

#2   
@client.command(name='ShutDown', help='Turns Off the Bot')
async def ShutDown(ctx):
    if str(ctx.message.author.id) in admin_usr:
        print("Information[ShutDown]: Started turning off the Bot")
        try:
            print("Information[ShutDown]: Saving Logs.txt...")
            src = open(f'{maindir}/Logs.txt', 'r')
            logs = open(f'{maindir}/Files/Logs.txt', 'a')
            append = f"\n\n{src.read()}"
            logs.write(append)
            logs.close()
            src.close()
            print("Logs.txt saved successfully.")
        except:
            print("Error occurred while saving log.")
        print("Information[ShutDown]: Shutting Down...")
        await ctx.send(f'ClosingBot.')
        await asyncio.sleep(1)
        await ctx.send(f'ClosingBot..')
        await asyncio.sleep(1)
        await ctx.send(f'ClosingBot...')
        await asyncio.sleep(1)
        exit()
    else:
        await ctx.reply(not_allowed)

#3
@client.command(name='testbot', help='Tests some functions of Host and Bot')
async def testbot(ctx):
    if str(ctx.message.author.id) in mod_usr:
        teraz = datetime.datetime.now()
        await ctx.send(f"""
***S e r v e r  B o t***  *test*:
====================================================
Time: **{teraz.strftime('%d.%m.%Y, %H:%M:%S')}**
Bot name: **{client.user}**
Version: **{ver}**
DisplayName: **{displayname}**
CPU Usage: **{psutil.cpu_percent()}** (%)
CPU Count: **{psutil.cpu_count()}**
CPU Type: **{testbot_cpu_type}**
RAM Usage: **{psutil.virtual_memory().percent}** (%)
Ping: **{round(client.latency * 1000)}ms**
OS Test (Windows): **{psutil.WINDOWS}**
OS Test (MacOS): **{psutil.MACOS}**
OS Test (Linux): **{psutil.LINUX}**
OS Version: **{platform.version()}**
OS Kernel: **{platform.system()} {platform.release()}**
Bot Current Dir: **{os.getcwd()}**
Bot Main Dir: **{maindir}**
File size: **{os.path.getsize(f'{maindir}/ServerBot.py')}**
Floppy: **{os.path.exists('/dev/fd0')}**
====================================================""")
    else:
        await ctx.send(not_allowed)
        #Other Essential Commands - END


        #Test_Commands
#1
#@client.command(name='test', help='test', tts=True)
#async def test(ctx):
#    await ctx.send(f'test {ctx.author.mention}')

#2
#@client.command(name='ServerKiller', help="Don't use this")
#async def kill(ctx):
#    while True:
#        await ctx.send('@everyone')
#
        #Test_Commands-END



################################################ S L A S H   C O M M A N D S ###########################################################################################
#1
@client.tree.command(name='random', description='Shows your random number. Type .random [min] [max]')
@app_commands.describe(min="Minimum value", max="Maximum value")
async def random_slash(interaction: discord.Interaction, min: int, max: int):
    import random
    try:
        randomn = random.randrange(min, max)
        await interaction.response.send_message(f'This is your random number: {randomn}')
    except Exception as error:
        if extendedErrMess:
            await interaction.response.send_message(f'{random_err}\nPossible cause: {error}')
        else:
            await interaction.response.send_message(random_err)

#2
@client.tree.command(name='testbot', description='Tests some functions of Bot')
async def testbot(interaction):
    if str(interaction.user.id) in mod_usr:
        teraz = datetime.datetime.now()
        await interaction.response.send_message(f"""
    ***S e r v e r  B o t***  *test*:
    ====================================================
    Time: **{teraz.strftime('%d.%m.%Y, %H:%M:%S')}**
    Bot name: **{client.user}**
    Version: **{ver}**
    DisplayName: **{displayname}**
    CPU Usage: **{psutil.cpu_percent()}** (%)
    CPU Count: **{psutil.cpu_count()}**
    CPU Type: **{testbot_cpu_type}**
    RAM Usage: **{psutil.virtual_memory().percent}** (%)
    Ping: **{round(client.latency * 1000)}ms**
    OS Test (Windows): **{psutil.WINDOWS}**
    OS Test (MacOS): **{psutil.MACOS}**
    OS Test (Linux): **{psutil.LINUX}**
    OS Version: **{platform.version()}**
    OS Kernel: **{platform.system()} {platform.release()}**
    Bot Current Dir: **{os.getcwd()}**
    Bot Main Dir: **{maindir}**
    File size: **{os.path.getsize(f'{maindir}/ServerBot.py')}**
    Floppy: **{os.path.exists('/dev/fd0')}**
    ====================================================""")
    else:
        await interaction.response.send_message(not_allowed)
################################################ S L A S H   C O M M A N D S  - E N D #######################################################################################

try:
    client.run(os.getenv('TOKEN'))
except Exception as err:
    print(f"Can't load Bot Token!\nEnter valid Token in '.env' file!\nPossible cause: {err}")