import time
import sys, os
def getTime():
    return "    " + time.ctime(time.time())

from PIL import Image, ImageDraw, ImageFont

import configparser
config = configparser.ConfigParser()
config.read("config.ini")

try:
    game_version = config["Version information"]["game_version"]
    num_version = config["Version information"]["num_version"]
    game_channel = int(config["Channel information"]["channel"])
    cmd_channels = config._sections["Channels"]

except Exception as e:
    print("Renderer config error: ", e)
    game_version = "Null"
    num_version = "Null"
    game_channel = "0"



# Initialization
import random
global InventoryID
global player
global players
InventoryID = 0
try: font = ImageFont.truetype("FFFFORWA.TTF", 10)
except Exception as e: print("Renderer couldn't load font: ", e) 
img = Image.new('RGB', (640, 480), color = (73, 109, 137))
d = ImageDraw.Draw(img)
global userList
global userCount

import wsav
'''
color_list = {
    "discordcraftdev1": 255,
    "discordcraftdev2": 0
}
'''

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def getPlayerColor(channel, reference_dict, color_list):
    
    try:
        a = getKeysByValue(reference_dict, str(channel))
        b = a[0]
        print(b)
        print(reference_dict)
        print("getPlayerColor() Result: "+str(color_list[str(b)]))
        return color_list[b]
    except Exception as e:
        print("getKeysByValue(): ERROR ", e)

color_list = {}
for x in cmd_channels:
    color_list.update({str(x):random.randrange(0, 256)})

'''
# Block ID variables definition



 TERRAIN GENERATION V1
 
 DESCRIPTION: 
 Basic superflat world
 
 GENERATION block (y coord):
 AIR 8+
 GRASS 7
 DIRT 6 - 4
 STONE 3 - 1
 BEDROCK 1

 Makes a block
 
 '''

'''
--------------------------------------------------------------------
                            BLOCK CLASS
--------------------------------------------------------------------
'''
class block:

    air = 0
    grass = 1
    dirt = 2
    stone = 3
    bedrock = 4
    player = 5   # (Internaly counts as a block)
    water = 6

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
        # Gets color based on the block ID
        # Sorry for if/elif, there isnt switch/case in python :(
        color = None
        if id == 0: color = (73, 109, 137)  
        elif id == 1: color = (97, 216, 0)
        elif id == 2: color = (147, 130, 50)
        elif id == 3: color = (94, 94, 93)
        elif id == 4: color = (38, 38, 38)
        elif id == 5: color = (255, 0, 0)       #Player
        elif id == 6: color = (0, 102, 204)

        #Renders object
        d.rectangle([(x, y), (x+16, y-16)], fill=color, outline=(0,0,0), width=0) 
    def delete(self, x, y):
        d.rectangle([(x, y), (x+16, y-16)], fill=(73, 109, 137), outline=(0,0,0), width=0)
    def draw(self, x, y, id, channel):
        color_seed = getPlayerColor(channel, cmd_channels, color_list)
        random.seed(color_seed*1234)
        color_a = random.randrange(0, 256)
        random.seed(color_seed*2345)
        color_b = random.randrange(0, 256)
        random.seed(color_seed*3456)
        color_c = random.randrange(0, 256)
        print("Random Colors: ", color_a, color_b, color_c)
        #Renders object
        color = None
        if id == 0: color = (73, 109, 137)
        elif id == 1: color = (97, 216, 0)
        elif id == 2: color = (147, 130, 50)
        elif id == 3: color = (94, 94, 93)
        elif id == 4: color = (38, 38, 38)
        elif id == 5: color = (color_a, color_b, color_c)
        elif id == 6: color = (0, 102, 204)
        d.rectangle([(x, y), (x+16, y-16)], fill=color, outline=(0,0,0), width=0)
       #print("test: ", getPlayerColor(channel, cmd_channels, color_list))

# Creates a list containing 5 lists, each of 8 items, all set to 0

# Spawn player

#global player
#player = block(block.player, 4*16, 480-((8*16)+1))

players = {}
for x in cmd_channels:
    players.update({str(x):block(block.player, 4*16, 480-((8*16)+1))})

'''
def spawnPlayer():
    global player
    player = block(block.player, 4*16, 480-((8*16)+1))
'''
def spawnPlayers():
    global players
    players.update({str(x):block(block.player, 4*16, 480-((8*16)+1))})


def getPlayer(channel):
    global players
    try:
        print(players)
        a = getKeysByValue(cmd_channels, str(channel))
        return players[a[0]]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


'''
--------------------------------------------------------------------
                        WORLD GENERATOR
--------------------------------------------------------------------
'''

def GenerateWorld():
    # Generates a basic world
    w, h = 50, 40 # Size of the maximum amount of blocks in window (480p)
    global world
    world = [[block(0, f*16, 480-(h*16)) for f in range(w)] for g in range(h)]
    # Fixed text that displays current version 
    d.text((10,10), game_version, fill=(255,255,0), font=font)

    # Generates grass
    for x in range(40):
        world[x][7] = block(block.grass, x*16, 480-(7*16))

    # Generates dirt
    for x in range(40):
        world[x][6] = block(block.dirt, x*16, 480-(6*16))
    for x in range(40):
        world[x][5] = block(block.dirt, x*16, 480-(5*16))
    for x in range(40):
        world[x][4] = block(block.dirt, x*16, 480-(4*16))

    # Generates stone
    for x in range(40):
        world[x][3] = block(block.stone, x*16, 480-(3*16))
    for x in range(40):
        world[x][2] = block(block.stone, x*16, 480-(2*16))
    for x in range(40):
        world[x][1] = block(block.stone, x*16, 480-(1*16))

    # Generates bedrock
    for x in range(40):
        world[x][0] = block(block.bedrock, x*16, 480-(0*16))

    spawnPlayers()
    print("e")


'''
--------------------------------------------------------------------
                            PLAYER COMMANDS
--------------------------------------------------------------------
'''

def PlayerControls(command, player, channel):
    #fbb = world[int(player.x/16)][int(((480 - player.y)/16)-1)]
    #print(world[int(player.x/16)][int(((480 - player.y)/16)-1)].id)
    
    print("PlayerControls")
    
    global InventoryID
    if command == "l":
        player.delete(player.x, player.y)
        player.x = player.x - 16
        player.draw(player.x, player.y, player.id, channel)
        print("Left command: "+getTime())
    
    elif command == "r":
        player.delete(player.x, player.y)
        player.x = player.x + 16
        player.draw(player.x, player.y, 5, channel)
        print("Right command "+getTime())
    elif command == "b":
        '''
        Why does this work
        '''
        if InventoryID == 0:
            bbi = 3
        elif InventoryID == 1:
            bbi = 2
        elif InventoryID == 2:
            bbi = 1
        elif InventoryID == 3:
            bbi = 6

        player.y = player.y - 16

        player.draw(player.x, player.y, 5, channel); player.delete(player.x, player.y+16)

        world[int(player.x/16)][int(player.y/16)+1] = block(bbi, player.x, player.y+16)
        print("Build command" +getTime()) 

    elif command == "d":
        
        player.y = player.y + 16
        player.draw(player.x, player.y, player.id, channel)
        world[int(player.x/16)][int(player.y/16)] = block(0, player.x, player.y-16)
        print("Destroy command "+getTime())
    elif command == "w":
        print("bruh")
        print(channel)
        player.delete(player.x, player.y)
        player.y = player.y - 16
        player.draw(player.x, player.y, 5, channel)
        print("Up command "+getTime())

    elif command == "i":
        print("Inventory command "+getTime())
        if InventoryID == 3:
            InventoryID = 0
        else:
            InventoryID += 1
    else:
        return "Invalid command!"


userCount = 0
userList = [None]

'''
--------------------------------------------------------------------
                        IMAGE RENDERING
--------------------------------------------------------------------
'''

def Render(user, channel):
    x = 1
    userList = ["Null"]
    UserAlreadyExists = False
    if user in userList:
        UserAlreadyExists = True

    a = user.split("#")[0]

    if UserAlreadyExists == False:
        print("Renderer.Render(): user appended -> ", a)
        userList.append(a)
        color_seed = getPlayerColor(channel, cmd_channels, color_list)
        random.seed(color_seed*1234)
        color_a = random.randrange(0, 256)
        random.seed(color_seed*2345)
        color_b = random.randrange(0, 256)
        random.seed(color_seed*3456)
        color_c = random.randrange(0, 256)
        d.text((10,50+(20*x)), "User: "+userList[x], fill=(color_a, color_b, color_c), font=font)
        x = x + 1
    #wsav.Save("save/world.save", world)
    img.save('imgrender/render.png')
