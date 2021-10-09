import discord
import random
from discord.ext import commands

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
         "\N{Regional indicator symbol letter O}", # "\N{Regional indicator symbol letter N}",
         "\N{Regional indicator symbol letter G}", "\N{Regional indicator symbol letter U}",
         "\N{Regional indicator symbol letter S}"],
        ["\N{Regional indicator symbol letter I}", "\N{Regional indicator symbol letter M}",
         "\N{Regional indicator symbol letter P}", "\N{Regional indicator symbol letter O}",
         "\N{Regional indicator symbol letter S}", "\N{Regional indicator symbol letter T}", "0️⃣",
         "\N{Regional indicator symbol letter R}"],
        [:amongus:751566927196848198], [:black:777321141450309632], 
        [:cyan:758808248366923776], [:lime:777321143991926784], 
        [:magenta:777321143442341908], [:orange:777321887520915477], 
        [:green:774402054307315713], [:red:774401387136024596], 
        [:purple:777321143715627039], [:white:777321142683172936],
        [:embarsus:890299247583440906]
    ]
    choice = options[random.randrange(len(options))]
    for item in choice:
        await msg.add_reaction(item)


@bot.event
async def on_message(message):
    if message.author.bot: return

    if "sus" in message.content and not message.content.startswith("%owofy"):
        await message.channel.send("amogus")

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


tok = ""
bot.load_extension('jishaku')
bot.run(tok)
