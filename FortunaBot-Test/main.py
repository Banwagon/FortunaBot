#Fortuna Discord Bot

import discord, os, random, asyncio
#import requests, json, webbrowser

from discord.ext import commands
#from bs4 import BeautifulSoup

#### Code for Testing Only, Do not use in Live Enviroment ####
from dotenv import load_dotenv #For testing Only
load_dotenv() #For Testing Only
brice = os.getenv("brice") #For Testing Only
my_secret = os.getenv("passcode") #For Testing only

#Variables
client = commands.Bot(command_prefix='$')  #sets command prefix as $
##brice = os.environ['brice'] #For live use only
##my_secret = os.environ['passcode']  #For live only

#### Set Bot Activity ####
@client.event
async def on_ready():  #will post when bot is ready
    ##Setting `Playing` status##
    #await client.change_presence(activity=discord.Game(name="a game"))
    await client.change_presence(activity=discord.Game(name="Visual Studio Code")) #For Testing Only
    ##Setting `Streaming` status##
    #await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    ##Setting `Listening` status##
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    ##Setting `Watching` status##
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Brice Undress \U0001f44C"))  #Sets bots status to Watching Brice Undress :ok_hand:
    print('Bot is ready, logged in as {0.user}'.format(client))  #console print that the bot is online as username

#### Embeds ####
#embed=discord.Embed(
    #title="Sample Embed", 
    #url="https://realdrewdata.medium.com/", 
    #description="This is an embed that will show how to build an embed and the different components",
    #color=0x109319
    #)

## Add author, thumbnail, fields, and footer to the embed ##
#embed.set_author(
    #name="RealDrewData",
    #url="https://twitter.com/RealDrewData",
    #icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg"
    #)
#embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
#embed.add_field(
    #name="Field 1 Title",
    #value="This is the value for field 1. This is NOT an inline field.",
    #inline=False) 
#embed.add_field(
    #name="Field 2 Title",
    #value="It is inline with Field 3",
    #inline=True)
#embed.add_field(
    #name="Field 3 Title",
    #value="It is inline with Field 2",
    #inline=True)
#embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")

## User's display name in the server
#ctx.author.display_name

## User's avatar URL
#ctx.author.avatar_url

masked_link_embed = discord.Embed(
    #title = 'Click here for a good time',
    description='You have just rolled a **69** for your lord and savior, <@{}> the waifu king.  [Click here to honor your Senpai.](https://www.youtube.com/watch?v=iik25wqIuFo)'.format(brice),
    color=15844367
    )

#### Direct Message ####
@client.command()
async def send_dm(ctx, member: discord.Member, *, content): #$send_dm <user> <message>
    channel = await member.create_dm()
    await channel.send(content)

#### Webhooks ####


#### WebScrapping ####

#### Purge Command ####
@client.command()
async def purge(ctx, amount=5):  #$purge command, 5 messages
    await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)  #$purge 10 - will purge 10 messages, will not purge pinned messages.

#### Roll Command ####
@client.command()
async def roll(ctx):
    #if str(ctx.message.channel) == "🎲-＄roll-for-items" and ctx.message.content != "": #limits commands to channel and with content
    if ctx.message.author.id == brice:  #Added as the Brice-variant
        await ctx.send(f"{ctx.message.author.mention} rolled 69 (69-69), Just Becasue.", delete_after=120)  #Added as the Brice-variant
        await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
        await ctx.message.delete()  #deletes the users message
    if ctx.message.author.id != brice:  #Added as the Brice-variant
        await ctx.send(f"{ctx.message.author.mention} rolled {random.randint(1,100)} (1-100)", delete_after=120)
        await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
        await ctx.message.delete()  #deletes the users message

#### Brice Command ####
@client.command()  #Added as the Brice-variant
async def brice(ctx):  #Added as the Brice-variant
    #await ctx.send(f"{ctx.message.author.mention} rolled a 69 (69-69) for <@{}>, the waifu king.".format(brice), delete_after=120) #Added for Brice
    await ctx.send(embed=masked_link_embed, delete_after=120)
    await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
    await ctx.message.delete()  #deletes the users message

#### Loot Command ####
@client.command(aliases=['loot'])
async def question(ctx, *, question):
    await ctx.send(f'{ctx.author.mention} has started the lottery for: **{question}**\n\nPlease __**$roll**__ if you are interested.', delete_after=120)
    await asyncio.sleep(120)  #puts the next commant to sleep for (120) seconds
    await ctx.message.delete()  #deletes the users message
    ##Alternate Formt##
    #await ctx.send(f'{ctx.author.mention} has started the lottery for: __**{question}**__\n\n{ctx.message.guild.default_role} please __**$roll**__ if you are interested.')

#### Discord Key ####
client.run(my_secret)  #Calls forward hidden KEY
