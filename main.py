from asyncio.tasks import sleep
from collections import namedtuple
from datetime import date
from inspect import ArgInfo
import os
import asyncio
import re
from pyasn1_modules.rfc2459 import CountryName
import serial
import random
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
import random
import time
from discord.utils import get
from pyyoutube import Api
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from pymongo import MongoClient, collation, collection, results                                                                      
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
cluster = MongoClient("mongodb+srv://Armaan:Armaanmar2020*@cluster0.oqnly.mongodb.net/Ytbot?retryWrites=true&w=majority")    
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from discord import message
from discord.ext.commands import bot
from discord.ext.commands.cooldowns import BucketType 
from discord import Colour
from discord.ext.commands.errors import MemberNotFound 
from googleapiclient.discovery import build

# Create YouTube Object
api = Api(api_key='AIzaSyC-lFsU6FJSFFr9lXlZ_H9Tm86TL2QnSuE')
TOKEN = "ODQzMzgxOTE4OTAzODI4NDkw.YKDCng.Qsrjoix11Y1eew32lnPRR1p0nvU"
intents = discord.Intents.default()
intents.members = True


# ser = serial.Serial('COM6', 9600)
bot = commands.Bot(command_prefix ='!',intents=intents)
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def r(ctx,arg):

    number = int(arg)
    random_number = random.randrange(11)

    if   random_number != number:
            print('Your random number is', random_number, 'LMAO YOU LOST')
            embed2 = discord.Embed(title="", description="      ",inline = False) 
            
            embed2.set_image(url="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
            embed2.set_footer(text="Number being Rolled for: {}".format(ctx.author.display_name))
            ms = await ctx.send(embed=embed2)
            time.sleep(4)
            print('Your random number is', random_number, 'LMAO YOU LOST')
            embed = discord.Embed(title="LMAO YOU LOST", description=f"Bot rolled  {random_number} ",colour=0xff0000) 
            embed.add_field(name="ADVICE", value="Get some better luck next time.",inline= 
            True)
            embed.set_thumbnail(url="https://media1.tenor.com/images/518a56fe36b41bc039b812ab2725e475/tenor.gif?itemid=21817747")
           
            embed.set_footer(text="Number rolled by: {}".format(ctx.author.display_name))
            
            await ms.edit(embed=embed)
    
    
    elif random_number == number :
             embed2 = discord.Embed(title="", description="") 
            
             embed2.set_image(url="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
             embed2.set_footer(text="Number being Rolled for: {}".format(ctx.author.display_name))
             ms = await ctx.send(embed=embed2)
             time.sleep(4)
             print('Your random number is', random_number,
                  'LUCKY DUCKY YOU WON')
             embed = discord.Embed(title="LUCKY DUCKY YOU WON", description=f"Bot rolled  {random_number} ",colour= 0x00ff00) 
             embed.add_field(name="ADVICEe", value="You dont need any advice.",inline=
             False)
             embed.set_thumbnail(url="https://i.pinimg.com/originals/aa/a8/2c/aaa82c7a835628871ef8a7e0c276dfb8.gif")
            
             embed.set_footer(text="Number rolled by: {}".format(ctx.author.display_name))
             await ms.edit(embed=embed)
             
           
           
@bot.event       
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="COOLDOWN", description="",colour=0x000000) 
            embed.add_field(name="TIME LEFT", value="Try again in {:.2f}s".format(error.retry_after),inline=  False)
           
            embed.set_thumbnail(url="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
            embed.set_footer(text="IDIOT: {}".format(ctx.author.display_name))
            await ctx.send(embed=embed) 
@bot.command()
async def help1(ctx):
     embed = discord.Embed(title="HELP IS HERE", description="",    colour=0x000000) 
     embed.add_field(name="ROLL A NUMBER", value=" Hi there To play the game use the command !r and your number (1-10) if your  entered number is same and the random number taken by the    machine then u win else u are a loser example command - !r 2", inline= False)
     await ctx.send(embed=embed)   


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(851419618856796188)
    embed=discord.Embed(title="Welcome To Ardupy!",description=f"{member.mention} ")
    embed.add_field(name = "VERIFY YOURSELF",value= "Verify yourself by typing verify below:")
    await channel.send(embed=embed)


@bot.listen('on_message')
async def whatever_you_want_to_call_it(message):
     if message.author == client.User:
                                      return

     elif message.content == "verify" :
        rn1 = random.randrange(10000)           
        embed = discord.Embed(title ="VERIFY YOURSELF",description = "verfy your self by typing the following code: {}".format(rn1),colour =0x000000)  
                            
        await message.channel.send(embed=embed)    
        channel = message.channel
        



        # do stuff      
        
        def check(m):
          return    m.author == message.author and m.author != client.User and channel == m.channel

        
        message = await bot.wait_for("message",timeout =12,check = check)
        content = int(message.content)
        print(content)
        if content != rn1 :
                embed1 = discord.Embed(title ="   Verifing",colour = 0x000000)
                embed1.set_image(url ="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
                msg = await message.channel.send(embed=embed1)
                time.sleep(4)
                embed = discord.Embed(title ="RETRY AGAIN : ",description = "WRONG CODE ENTERED : Retry again in 5 minutes :{}".format(message.author),colour =0xff0000)  
                            
                await msg.edit(embed=embed)  
                print("idiot:{}".format(message.author))
        if content == rn1:
                 embed1 = discord.Embed(title ="   Verifing",colour = 0x000000)
                 embed1.set_image(url ="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
                 msg = await message.channel.send(embed=embed1)
                 time.sleep(4)  
                 print("verified")
                 embed = discord.Embed(title ="VERIFIED ", description = "verified :{}".format(message.author),colour =0x00ff00,inline =True)  
                 embed.add_field(name="CHOOSE YOUR ROLES",value=" . ")
                 embed.add_field(name="Arduino",value="react with :arduino:")
                 embed.add_field(name="c++",value="react with :javascript:")
                 member = message.author
                 await msg.edit(embed=embed)  
                 role = discord.utils.get(member.guild.roles, name="Verified")
                 print(role)
                 await member.add_roles(role)
                 await msg.add_reaction('✅')
                 await msg.add_reaction('❌')
               
                 def check(reaction, user):
                         return str(reaction.emoji) in ['✅', '❌'] and message.author != bot.user

  
                 reaction, user = await bot.wait_for('reaction_add', check=check, timeout=60)



                 x = 1
                 if str(reaction.emoji) == '✅':
                         await channel.send("You reacted with the ✅ emoji")
 
                 if str(reaction.emoji) == '❌':
                              await channel.send("You reacted with the ❌ emoji")
               

@bot.listen('on_message')
async def w(message):
        
        if "<@!843381918903828490>" in message.content:
            embeds = discord.Embed(title = "",description = f"  {message.author} Dont Mention me once more  or i will burn u in :fire") 
            await message.channel.send(embed= embeds)
            print(message.content)

@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))  
    print(' {:.2f}ms'.format(duration))
    

@bot.command()
async def shutdown(ctx):
       if ctx.author.id == 794513708008603658:
         embeds = discord.Embed(title = "Shutingdown.....",description = " shutdown requested by {}".format(ctx.author))
        
         embeds.set_thumbnail(url ="https://bestof.nyc3.digitaloceanspaces.com/devsnap.me/sam/staggered-wave-loading.gif")
         message = await ctx.send(embed = embeds)
         time.sleep(5)
         embed1 = discord.Embed(title = "Shutdown complete",description =  "shutdown requested by {}".format(ctx.author))
         
         await message.edit(embed = embed1)
         await bot.close()
       else :
                
                 embed5 = discord.Embed(title ="Warning !",description = f" {ctx.message.author.mention} you are not allowed to use this command :: <@!794513708008603658> has been reported ")
                 await ctx.send(embed =embed5)


# VC PROCESSING
@bot.event
async def on_voice_state_update(member, before, after):
      if member.id ==794513708008603658:
     
       if not before.self_mute and after.self_mute:
           print("muted")
        #    time.sleep(0.1) 
        #    ser.write(b'M') 
          
       elif before.self_mute and not after.self_mute:
            #  time.sleep(0.1)
            #  ser.write(b'U')
           
             print("unmuted")
        
@bot.listen('on_message')
async def wt_to_call_it(message):
    if message.author == bot.user:
        return
        
    hello_quotes = [
'hello','Hello','hi','HI', 'Hi','sup','SUP','ello', 'namaste','NAMASTE'
    ]

    if message.content == 'hello'or message.content =='Hello'or message.content =='hi'or message.content =='HI'or  message.content =='Hi'or message.content =='sup'or message.content =='SUP'or message.content =='ello'or message.content =='namaste'or message.content =='NAMASTE':
        response = random.choice(hello_quotes)
        await message.channel.send(response)

@bot.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    voice = get(self.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

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
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
       
        

  
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
         msg12 = "Unlinked"
    await ctx.send(msg12)
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
				developerKey='AIzaSyC-lFsU6FJSFFr9lXlZ_H9Tm86TL2QnSuE')

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
    embed.add_field(name = "Link",value ="https://www.youtube.com/channel/{}".format(results['acc']))
    embed.add_field(name = "Country",value =CountryName)
    
    
    embed.set_thumbnail(url="{}".format(done))
    await ctx.send(embed = embed)
bot.run(TOKEN)








 
