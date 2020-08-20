import sys
sys.path.append('lib')

import wsav


import configparser
config = configparser.ConfigParser()
config.read("config.ini")

game_version = config["Version information"]["game_version"]
num_version = config["Version information"]["num_version"]
game_channel = int(config["Channel information"]["channel"])

import renderer
import time
import discord
import console
from discord.ext import commands



global FirstMSG
FirstMSG = True

def getTime():
    return "    " + time.ctime(time.time())
def divline():
    print ("------------")

divline()
print("UnsuccesfulHttp DiscordCraft made in July 2020 - August 2020")
print("Current game version: "+game_version)
print("Bot program started!"+getTime())
divline()

myself = "Test434365345334543#6642"

Inventory = "Stone Dirt Grass"


client = commands.Bot(command_prefix="!")

'''
--------------------------------------------------------------------
                            ON MESSAGE
--------------------------------------------------------------------
'''

@client.event                                                                                           
async def on_message(message):
    print("Message detected: ",getTime())
    global FirstMSG                                                                                     
    global InventoryID
    global Inventory
    Inventory = " "
    

    if message.channel != client.get_channel(game_channel): return
    if message.author == client.user:
        time.sleep(1)
        if FirstMSG == True:
            await message.add_reaction("🔄")
            FirstMSG = False
            return
        else: 
            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")
            await message.add_reaction("⬆️")
            await message.add_reaction("🔨")
            await message.add_reaction("🔧")
            await message.add_reaction("📦")
            await message.add_reaction("💾")
            await message.add_reaction("📥")
        return
    
    print("Message detected!"+getTime())

    if message.mention_everyone: await message.channel.send("D O N T P I N G @everyone"); print(message.author)
    elif message.content.startswith("render"): renderer.GenerateWorld(); print("Render command "+getTime())
    elif message.content.startswith("l"):print("Left command "+getTime())
    elif message.content.startswith("r"):print("Right command "+getTime())  
    elif message.content.startswith("b"):print("Build command" +getTime())   # e l s e i f 
    elif message.content.startswith("d"):print("Destroy command "+getTime())   
    elif message.content.startswith("w"):print("Up command "+getTime()) 
    elif message.content.startswith("i"):print("Inventory command "+getTime())
    elif message.content.startswith("fload"):global world; renderer.world = wsav.Load("save/world.save "); print("Load command "+getTime())
    elif message.content.startswith("save"):
        wsav.Save("save/world.save", renderer.world)
        print("Save command "+getTime())
        embed = discord.Embed(title="**Game saved!**", color=0x00ff00)
        await message.channel.send(embed=embed)

    print("h")
    try: renderer.PlayerControls(message.content)
    except Exception as e: print("PlayerControls Error: ", e)
    
    renderer.Render(str(message.author))


    if renderer.InventoryID == 0: Inventory = "**Stone** Dirt Grass Water"
    elif renderer.InventoryID == 1: Inventory = "Stone **Dirt** Grass Water"
    elif renderer.InventoryID == 2: Inventory = "Stone Dirt **Grass** Water"
    elif renderer.InventoryID == 3: Inventory = "Stone Dirt Grass **Water**"

    embed = discord.Embed(title=game_version+" Playable Embed", description="**Controlls:** \n -  **render:** Makes new world \n -  **l and r:** Move to left/right \n -  **b and d:** Build / Destroy \n -  **w:** Move upwards \n \n **WARNING: This bot is in early development**", color=0x00ff00) #creates embed
    file = discord.File("imgrender/render.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    embed.add_field(name="**Inventory**", value=Inventory)
    await message.channel.send(file=file, embed=embed)
    
    divline()
    #await console.console_input()
'''
--------------------------------------------------------------------
                            ON READY
--------------------------------------------------------------------
'''
@client.event                                                                                           
async def on_ready():                                                                                   
    global InventoryID
    InventoryID = 0
    print("Bot is ready"+getTime())
    divline()
    channel = client.get_channel(game_channel)
    embed = discord.Embed(title="Bot has started! :computer:", description="For starting a world say: **render** or react with :arrows_counterclockwise: , otherwise it will just display a blank screen", color=0x00ff00)
    embed.set_footer(text=game_version + "  |  Version number: "+num_version)
    await channel.send(embed=embed)
    global FirstMSG
    FirstMSG = True
    #await console.console_begin()
    
'''
--------------------------------------------------------------------
                          ON REACTION ADD
--------------------------------------------------------------------
'''


@client.event
async def on_reaction_add(reaction, user):

    print("Reaction added! "+str(getTime()))
    global Inventory
    global InventoryID
    command = " "
    if user == client.user: return
    if reaction.emoji == "🔄":renderer.GenerateWorld();print("Render command")
    elif reaction.emoji == "⬅️":print("Left command"); command = "l"
    elif reaction.emoji == "➡️":print("Right command"); command = "r"  
    elif reaction.emoji == "⬆️":print("Build command"); command = "w"
    elif reaction.emoji == "🔨":print("Destroy command"); command = "d"
    elif reaction.emoji == "🔧":print("Up command"); command = "b"
    elif reaction.emoji == "📦":print("Inventory command"); command = "i"
    elif reaction.emoji == "💾":
        wsav.Save("save/world.save", renderer.world)
        print("Save command "+getTime())
        channel = reaction.message.channel
        embed = discord.Embed(title="**Game saved!**", color=0x00ff00)
        await channel.send(embed=embed)
    elif reaction.emoji == "📥":global world; renderer.world = wsav.Load("save/world.save "); print("Load command "+getTime())
    
    try: renderer.PlayerControls(command)
    except Exception as e: print("Error: ", e)
    renderer.Render(str(user.name))

    divline()

    if renderer.InventoryID == 0: Inventory = "**Stone** Dirt Grass Water"
    elif renderer.InventoryID == 1: Inventory = "Stone **Dirt** Grass Water"
    elif renderer.InventoryID == 2: Inventory = "Stone Dirt **Grass** Water"
    elif renderer.InventoryID == 3: Inventory = "Stone Dirt Grass **Water**"

    channel = reaction.message.channel
    embed = discord.Embed(title=game_version+" Playable Embed", description="**Controlls:** \n -  **🔄 render:** Makes new world \n -  **⬅️ l and ➡️ r:** Move to left/right \n -  **🔧 b and 🔨 d:** Build / Destroy \n -  **⬆️ w:** Move upwards \n \n **WARNING: This bot is in early development**", color=0x00ff00) #creates embed
    file = discord.File("imgrender/render.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    embed.add_field(name="**Inventory**", value=Inventory)
    await channel.send(file=file, embed=embed)
    renderer.Render(str(user))

bot_token = open("token/botToken.txt", "r")
client.run(bot_token.read())

