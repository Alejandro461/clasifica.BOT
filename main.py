import discord
from discord.ext import commands
from modelo import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name=attachment.filename
            file_url=attachment.url
            await attachment.save(file_name)
            try:
                await ctx.send("archivo guardado")
                class_name = get_class("keras_model.h5","labels.txt",file_name)
                if class_name == "Gorriones":
                    await ctx.send("esto es un gorrion y los gorriones son aves comunes y sociables, conocidas por su adaptación a entornos urbanos y rurales. Son aves pequeñas, robustas y muy adaptables")
                elif class_name == "Palomas":
                    await ctx.send ("esto es una paloma y las palomas son aves fascinantes con una serie de características y capacidades sorprendentes. Pueden vivir hasta 30 años")
            except:
                await ctx.send("ERROR, puede que no se pudiera clasificar su imagen o el formato de la imagen es incompatible")

    else:
        await ctx.send("imagen no adjunta")
bot.run("TOKEN")