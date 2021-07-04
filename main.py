
import discord

from pyyoutube import Api
from discord import client
from discord import colour
from discord import embeds
from discord import member
from discord import guild
from discord import channel
import discord.ext
from discord.ext import commands
import time
from discord.utils import get
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from pymongo import MongoClient, collation, collection, results                                                                      
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
cluster = MongoClient("mongodb+srv://Armaan:password:)@cluster0.oqnly.mongodb.net/database_name?retryWrites=true&w=majority")    
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from discord import message
from discord.ext.commands import bot



from googleapiclient.discovery import build

# Create YouTube Object
api = Api(api_key=token)
TOKEN = "uwu"
intents = discord.Intents.default()
intents.members = True


# ser = serial.Serial('COM6', 9600) ik this isnt needed but ok
bot = commands.Bot(command_prefix ='y/',intents=intents) #i aint creating a dict for prefix :)

@bot.command()
async def link(ctx,arg):
  
  if arg.startswith("https://www.youtube.com/channel/"):
  
   db=cluster["Ytbot"]
   collection= db["Ytbot"]
   results = collection.find_one({"_id": "{}".format(ctx.author.id)})
   if results != None:
       msg2 = "acc already linked unlink a account to link another "
       await ctx.send(msg2)
   if results == None:
      
        msg = "account sent to mods for approval please comment on this vid"
        print(ctx.author.id)
        await ctx.send(msg )
        yourID = 794513708008603658
        discordUser =bot.get_user(yourID)

        msg = await discordUser.send("User :{}, channel :{}, Id: {}".format(ctx.author,arg,ctx.author.id))
        
       
        

  
        reaction, user = await bot.wait_for('reaction_add' )



                
        if str(reaction.emoji) == '❌':
                         await discordUser.send("REQUEST DECLINED for {}".format(ctx.author))
                         yourID = ctx.author.id
                         discordUser2 =bot.get_user(yourID)
                         msd = " Your account link has been  declined , contact mods if u think it was by mistake"
                         await discordUser2.send(msd)
                         
        if str(reaction.emoji) == '✅':
                              await discordUser.send("REQUEST ACCEPTED for {}".format(ctx.author))
                              db=cluster["Ytbot"]
                              collection= db["Ytbot"]
                              post = {"_id":"{}".format(ctx.author.id),"name":"{}".format(ctx.author),"acc":'{}'.format(arg[32:56])}
                              collection.insert_one(post)
                              yourID = ctx.author.id
                              discordUser2 =bot.get_user(yourID)
                              msd = " Your account link has been  accepted , enjoy "
                              await discordUser2.send(msd)
                         
  else:
            message = "Dont try to break me use something like this https://www.youtube.com/channel/<ur channel id>"
            await ctx.send(message)
    

@bot.command()
async def unlink(ctx):
    db=cluster["Ytbot"]
    collection= db["Ytbot"]
    results = collection.find_one({"_id": "{}".format(ctx.author.id)})
    if results == None:
        msg = "u havn't even linked and want to unlink smh"
        await ctx.send(msg)
    elif results != None:
         db=cluster["Ytbot"]
         collection= db["Ytbot"]
         results = collection.delete_one({"_id": "{}".format(ctx.author.id)})
         msg = "Unlinked"
    await ctx.send(msg)
@bot.command()
async def stats(ctx, member: discord.Member=None):
    member = member or ctx.author
    id1 = member.id
    db=cluster["Ytbot"]
    collection= db["Ytbot"]
    results = collection.find_one({"_id": "{}".format(id1)})
    print(results)
    if results == None:
       ok = "No accounts have been linked to {}".format(member)
       print(ok)
       await ctx.send(ok)
    elif results != None:
        
         print("acc exist")
        
    youtube = build('youtube', 'v3',
				developerKey='smh_u faker :)')

    ch_request = youtube.channels().list(
	part='statistics',
	id=results["acc"])

# Channel Information
    ch_response = ch_request.execute()

    sub = ch_response['items'][0]['statistics']['subscriberCount']
    vid = ch_response['items'][0]['statistics']['videoCount']
    views = ch_response['items'][0]['statistics']['viewCount']
    api = Api(api_key="AIzaSyC-lFsU6FJSFFr9lXlZ_H9Tm86TL2QnSuE")
    channel_by_id = api.get_channel_info(channel_id="{}".format(results["acc"]))
    done = channel_by_id.items[0].snippet.thumbnails.high.url
    title = channel_by_id.items[0].snippet.title
    date_published_channel = channel_by_id.items[0].snippet.publishedAt
    date_published_channel = date_published_channel[0:10]
    custom_url = channel_by_id.items[0].snippet.customUrl
    CountryName = channel_by_id.items[0].snippet.country
    owner = channel_by_id.items[0].snippet.localized.description
    
    
    print(done)
    
    print("Total Subscriber:- ", sub)
    print("Total Number of Videos:- ", vid)
    print("Total Views:- ", views)
    embed =discord.Embed(title = "{} 'stats".format(title),description = "")
    embed.add_field(name = "views",value = views)
    embed.add_field(name = "videos",value = vid)
    embed.add_field(name = "Subscribers",value = sub)
    embed.add_field(name = "description",value =owner)
    embed.add_field(name = "Channel made on",value = date_published_channel)
    embed.add_field(name = "Custom Url",value =custom_url)
    embed.add_field(name = "Channel ID",value = "{}".format(results['acc']))
    
    embed.add_field(name = "Country",value =CountryName)
    
    
    embed.set_thumbnail(url="{}".format(done))
    await ctx.send(embed = embed)
keep_alive()
bot.run(TOKEN)
