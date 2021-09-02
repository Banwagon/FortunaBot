import discord
import os
import requests
import json
import random
from bs4 import BeautifulSoup
import webbrowser
from replit import db
from discord.ext import commands
from keep_alive import keep_alive


#client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  print('Bot is ready, logged in as {0.user}'.format(client))

@client.command()
async def roll(ctx):
  if ctx.message.author.id == 214553002277732352: #Added for Brice
    await ctx.send(f"{ctx.message.author.mention} rolled 69 (69-69), Becasue Brice said so.") #Added for Brice
  if ctx.message.author.id != 214553002277732352: #Added for Brice
    await ctx.send(f"{ctx.message.author.mention} rolled {random.randint(1,100)} (1-100)")

@client.command() #Added for Brice
async def brice(ctx): #Added for Brice
  await ctx.send(f"{ctx.message.author.mention} rolled a 69 (69-69), _Becasue Brice said so_") #Added for Brice

@client.command(aliases=['loot'])
async def question(ctx, *, question):
  await ctx.send(f'{ctx.author.mention} has started the lottery for: __**{question}**__\n\nPlease __**$roll**__ if you are interested.')
  
  ##Alternate Formt##
  #await ctx.send(f'{ctx.author.mention} has started the lottery for: __**{question}**__\n\n{ctx.message.guild.default_role} please __**$roll**__ if you are interested.')

keep_alive()
my_secret = os.environ['passcode']
client.run(my_secret)
