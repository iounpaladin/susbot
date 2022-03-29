import discord
import random
from discord.ext import commands
import requests
from PIL import Image, ImageDraw
import urllib.request

bot = commands.Bot(command_prefix='%', description="Now with 100% more cringe!")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(
        activity=discord.Game(name="Among Sus"))


async def chooseReaction(msg):
    options = [
        ["\N{Regional indicator symbol letter S}", "\N{Regional indicator symbol letter U}", "5️⃣"],
        ["\N{Regional indicator symbol letter A}", "\N{Regional indicator symbol letter M}",
         "\N{Regional indicator symbol letter O}",  # "\N{Regional indicator symbol letter N}",
         "\N{Regional indicator symbol letter G}", "\N{Regional indicator symbol letter U}",
         "\N{Regional indicator symbol letter S}"],
        ["\N{Regional indicator symbol letter I}", "\N{Regional indicator symbol letter M}",
         "\N{Regional indicator symbol letter P}", "\N{Regional indicator symbol letter O}",
         "\N{Regional indicator symbol letter S}", "\N{Regional indicator symbol letter T}", "0️⃣",
         "\N{Regional indicator symbol letter R}"],
        [":amongus:751566927196848198"], [":black:777321141450309632"],
        [":cyan:758808248366923776"], [":lime:777321143991926784"],
        [":magenta:777321143442341908"], [":orange:777321887520915477"],
        [":green:774402054307315713"], [":red:774401387136024596"],
        [":purple:777321143715627039"], [":white:777321142683172936"],
        [":embarsus:890299247583440906"]
    ]
    choice = options[random.randrange(len(options))]
    for item in choice:
        await msg.add_reaction(item)


async def susiety(url, message: discord.Message):
    colours = "red orange yellow green blue indigo violet".split()
    i = 0

    data = requests.post(
        "https://api.deepai.org/api/sussy-detector-5055-dev",
        data={
            'image': url,
        },
        headers={'api-key': KEY}
    )

    js = data.json()
    sus_count = len(js["output"]["Objects"])
    conf = []

    with open("temp.png", "wb") as f:
        f.write(requests.get(url).content)
    image = Image.open("temp.png")
    draw = ImageDraw.Draw(image)

    for object in js["output"]["Objects"]:
        bb = object["bounding_box"]
        if object["confidence"] >= 0.7:
            # draw.rectangle(((bb[0], bb[1]), (bb[2], bb[3])), outline=colours[i])
            draw.rectangle(((bb[0], bb[1]), (bb[2] + bb[0], bb[3] + bb[2])), outline=colours[i])
            conf.append((object["confidence"], colours[i]))

            i += 1
            if i >= len(colours):
                i = 0
        else:
            sus_count -= 1

    image.save("out.png")

    if sus_count:
        await message.channel.send(" ".join([f"sus ({obj[1]} -- {round(obj[0] * 100)}% confident)" for obj in conf]), file=discord.File("out.png"))

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot: return

    if message.attachments and message.guild.id in [895462504946368552, 97102230594781184, 609496545569800192]:
        for attachment in message.attachments:
            url = attachment.url

            await susiety(url, message)

    if "sus" in message.content and not message.content.startswith("%owofy"):
        await message.reply("amogus")

    keywords = ["mogus", "impostor", "mongus"]
    msg = message.content.lower()
    for item in keywords:
        if item in msg:
            if message.author.id != 895445702518407208 and message.author.id != 895464659107344384 and "%owofy" not in message.content.lower():
                await chooseReaction(message)
                break

    await bot.process_commands(message)


@bot.command()
async def owofy(ctx, *, message):
    """OwOfy a message! Usage: %owofy [message]"""
    if message:
        id = ('<@%s>' % ctx.author.id)
        totranslate = message.replace("$owofy", "")
        totranslate = totranslate.replace("r", "w")
        totranslate = totranslate.replace("l", "w")
        totranslate = totranslate + ("\n - %s" % id)
        await ctx.send(totranslate)
    else:
        await ctx.send("You need to put a message after the command! (%owofy [message])")


# NOTE: You need to have FFMPEG and the amongus drip song in the bot files
# Also, replace the "[INSERT HERE]" stuff with the actual routes to the files
# for example, mine is
# C:/Users/[username]/Desktop/susbot/ffmpeg.exe
# C:/Users/[username]/Desktop/susbot/drip.mp3
# for the first and second inserts, respectively
from discord import FFmpegPCMAudio


@bot.command()
async def dripify(ctx):
    """Makes a voice channel drippy"""
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(executable="[INSERT HERE]", source="[INSERT HERE]")
        player = voice.play(source)
    else:
        await ctx.send("You must be in a voice channel to use this command!")


@bot.command()
async def undripify(ctx):
    """Undripify a voice channel"""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        ctx.send("I'm not in a voice channel!")


with open(".TOKEN") as f:
    tok = f.read()

with open(".KEY") as f:
    KEY = f.read()

bot.load_extension('jishaku')
bot.run(tok)
