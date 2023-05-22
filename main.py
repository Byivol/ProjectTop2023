import random

import disnake
from disnake.ext import commands

from config import TOKEN

bot = commands.Bot(command_prefix= "$",help_command=None,intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print("Я заработал!")

@bot.command()
async def hello(inter):
    await inter.send("Привет!")

@bot.slash_command()
async def hello(inter):
    await inter.send("Привет!")

@bot.slash_command()
async def hello_to(inter, member: disnake.Member):
    await inter.send(f"Пользователь {inter.author.mention} передает привет {member.mention}!")

@bot.command()
async def monetka(inter):
    monets = ["Орел","Решка"]
    await inter.send(f"Пользователь {inter.author.mention} подбросил монетку...")
    for i in range(3):
        await inter.send(".")
    await inter.send("Монетка упала на сторону - ",random.choice(monets))

bot.run(TOKEN)
