import discord
import os
#import requests
#import json
import random
import asyncio
#import webbrowser
#from bs4 import BeautifulSoup
#from replit import db
from discord.ext import commands
#from keep_alive import keep_alive
#from MaxEmbeds import EmbedBuilder
from boto.s3.connection import S3Connection

#keep_alive()  #script that will ping server
client = commands.Bot(command_prefix='$')  #sets command prefix as $
brice = os.environ['brice']

masked_link_embed = discord.Embed(  #embedded linkes
    #title = 'Click here for a good time',
    description=
    'You have just rolled a **69** for your lord and savior, <@{}> the waifu king.  [Click here to honor your Senpai.](https://www.youtube.com/watch?v=iik25wqIuFo)'.format(brice),
    color=15844367)

@client.event
async def on_ready():  #will post when bot is ready
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="Brice Undress \U0001f44C"))  #Sets bots status to Diablo 2 Reborn
    print('Bot is ready, logged in as {0.user}'.format(
        client))  #console print that the bot is online as username

@client.command()  #Purges Channel Messages
async def purge(ctx, amount=5):  #$purge command, 5 messages
    await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)  #$purge 10 - will purge 10 messages

@client.command()
async def roll(ctx):
    #if str(ctx.message.channel) == "🎲-＄roll-for-items" and ctx.message.content != "": #limits commands to channel and with content
    if ctx.message.author.id == brice:  #Added as the Brice-variant
        await ctx.send(
            f"{ctx.message.author.mention} rolled 69 (69-69), Just Becasue.",
            delete_after=120)  #Added as the Brice-variant
        await asyncio.sleep(
            120)  #puts the next commant to sleep for (120) seconds
        await ctx.message.delete()  #deletes the users message
    if ctx.message.author.id != brice:  #Added as the Brice-variant
        await ctx.send(
            f"{ctx.message.author.mention} rolled {random.randint(1,100)} (1-100)",
            delete_after=120)
        await asyncio.sleep(
            120)  #puts the next commant to sleep for (120) seconds
        await ctx.message.delete()  #deletes the users message

@client.command()  #Added as the Brice-variant
async def brice(ctx):  #Added as the Brice-variant
    #await ctx.send(f"{ctx.message.author.mention} rolled a 69 (69-69) for <@{}>, the waifu king.".format(brice), delete_after=120) #Added for Brice
    await ctx.send(embed=masked_link_embed, delete_after=120)
    await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
    await ctx.message.delete()  #deletes the users message

@client.command(aliases=['loot'])
async def question(ctx, *, question):
    await ctx.send(
        f'{ctx.author.mention} has started the lottery for: **{question}**\n\nPlease __**$roll**__ if you are interested.',
        delete_after=120)
    await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
    await ctx.message.delete()  #deletes the users message
    ##Alternate Formt##
    #await ctx.send(f'{ctx.author.mention} has started the lottery for: __**{question}**__\n\n{ctx.message.guild.default_role} please __**$roll**__ if you are interested.')

my_secret = os.environ['passcode']  #discord password, hidden in file
client.run(my_secret)  #call forward password
