import logging
import os
from configparser import SafeConfigParser
from random import randint
from random import randrange
import discord
from discord.ext import commands
from nudenet import NudeClassifier
from nudenet import NudeDetector
logging.basicConfig(level=logging.INFO)

config = SafeConfigParser()
config.read('config.ini')

bot_mode = config['bot']['mode']
debug = config.getboolean('bot', 'debug')
token = config['bot']['token']
clientid = config['bot']['clientid']
prefix = str(config['bot']['prefix'])
botperms = config['bot']['botperms']

denythreshold = config.getfloat('policy', 'denythreshold')
imgFormats = config['policy']['acceptedfiles'].split(',')
tieBreaker = config.getboolean('policy', 'allow_ties')

bot = commands.Bot(command_prefix=prefix)

detector = NudeDetector()
classifier = NudeClassifier()

dicto = {}
replies = [
        "Dont send demeaning images {}?",
        "We classified your image as unsafe, Dont do that again {}.",
        "Grow up {}, kid",
        "What is this immature behaviour? {}.",
        "That is sooo wrong, If you keep doing it, this discord server would be a better place with you {}."
    ]


@bot.event
async def on_ready():
    invlink = f"https://discord.com/oauth2/authorize?client_id={clientid}&permissions={botperms}&scope=bot"
    print(f"I am GotYouCovered Bot, I delete bad adult images that are demeaning to women, Invite me at -> {invlink}")
    if debug:
        print(
            "==== WARNING: DEBUG MODE IS ON! NO MESSAGES WILL BE DELETED.====\n==== FOR THIS BOT TO MODERATE PROPERLY, "
            "TURN OFF DEBUG IN CONFIG.INI ====")

def scoreGet(imgloc):
    if debug:
        print(detector.detect(imgloc))
    safetyScore = classifier.classify(imgloc)[imgloc]
    os.remove(imgloc)
    if debug:
        print(safetyScore)
    if safetyScore['safe'] > safetyScore['unsafe'] and safetyScore['safe'] - safetyScore['unsafe'] > denythreshold:
        return 'safe'
    elif safetyScore['unsafe'] > safetyScore['safe'] and safetyScore['unsafe'] - safetyScore['safe'] > denythreshold:
        return 'unsafe'
    else:
        return 'tie'

def checkuser(uid):
    uid = '<@' + str(uid) + '>'
    t = randrange(5)
    usr = replies[t]
    usr = usr.format(uid)

    return usr


@bot.event
async def on_message(message):
    if len(message.attachments) > 0:
        for a in message.attachments:
            for f in imgFormats:
                if a.filename.lower().endswith(f):
                    saveloc = f'{randint(1, 1000)}{a.filename}'
                    await a.save(saveloc)
                    safetyScore = await bot.loop.run_in_executor(None, scoreGet, saveloc)
                    if debug:
                        print(f'User: {str(message.author)}, Score: {safetyScore}')
                    else:
                        if safetyScore == "unsafe":
                            print(f'Bad Message from User: {str(message.author)} was deleted and count was increased.')
                            await message.delete()
                            embed = discord.Embed(
                                title='Unsafe content removed',
                                color=discord.Colour.red(),
                                description=f"I have deleted a demeaning image from @{str(message.author)} as it was unsafe."
                                            f"GotYouCovered Bot has got you covered! Don't Worry!")
                            embed.set_footer(text=f"Contact admin if it was not a bad image and was misclassified")
                            await message.channel.send(embed=embed)
                        if safetyScore == "tie":
                            if not tieBreaker:
                                await message.delete()
                                print(f'This message was almost classified as unsafe. To be safe and secured, I have deleted an img from{str(message.author)}')
                                embed = discord.Embed(
                                    title='Demeaning Image was removed',
                                    color=discord.Colour.orange(),
                                    description=f"I have deleted a demeaning image from @{str(message.author)} as it was unsafe."
                                                f"GotYouCovered Bot has got you covered! Don't Worry!")
                                embed.set_footer(text=f"Contact admin if it was not a bad image and was misclassified.")
                                await message.channel.send(embed=embed)
                    user_id = message.author.id
                    if safetyScore == 'unsafe' or safetyScore == 'tie':
                        await message.channel.send(checkuser(user_id))
                        await message.channel.send(checkuser(user_id))
                        uid=str(str(message.guild.id)+"."+str(message.author))
                        if uid not in dicto:
                            dicto[uid] = 1
                        else:
                            dicto[uid] += 1
                        if dicto[uid] == 2:
                            reply = str("Another bad image and you are out of this server! <@" + str(user_id) + ">")
                            await message.channel.send(reply)
                        elif dicto[uid] > 2:
                            await message.author.kick()
    await bot.process_commands(message)


bot.run(token)
