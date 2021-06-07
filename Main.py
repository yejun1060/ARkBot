import discord, json
from discord.ext import commands

bot = commands.Bot(command_prefix="#")
with open('secret_setting.json') as j:
    data = json.load(j)
    code = data["code"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("#help로 명령어 보기"))
    print("ok-01")


bot.run(code)