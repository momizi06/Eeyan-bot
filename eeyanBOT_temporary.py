
# coding: utf-8

import discord.ext.commands
import asyncio
import random
import sys
import os


bot = discord.ext.commands.Bot(command_prefix="e!")
gamestatus = discord.Game("v0.0.1")

token = "unknown"

# ええやん返信内容
eeyanlist = ['ええやん', 'ええんちゃう？', 'おーええやん', '良き']


# 初期化と起動チェック用
@bot.event
async def on_ready():
    print('We have logged by {0.user}'.format(bot))
    await bot.change_presence(status = discord.Status.idle,  activity = gamestatus)

# ええやん返信用
@bot.event
async def on_message(message):
    if message.content.startswith("ええやん"):
        await message.channel.send(random.choice(eeyanlist))

# aboutコマンド
@bot.command(name="about")
async def about(ctx):
    # aboutコマンド用
    aboutembed = discord.Embed(title="このBotについて", description="ネタで作ってみました。")
    aboutembed.add_field(name="開発者", value="momizi06#5834")

    await ctx.send(embed=aboutembed)

# Botの稼働
bot.run(token)