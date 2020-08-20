
from PIL import Image, ImageDraw, ImageFont

import configparser
config = configparser.ConfigParser()
config.read("config.ini")

try:
    game_version = config["Version information"]["game_version"]
    num_version = config["Version information"]["num_version"]
    game_channel = int(config["Channel information"]["channel"])
except Exception as e:
    print("Renderer config error: ", e)
    game_version = "Null"
    num_version = "Null"
    game_channel = "0"

# Initialization
global InventoryID
global player
InventoryID = 0
try: font = ImageFont.truetype("FFFFORWA.TTF", 10)
except Exception as e: print("Renderer couldn't load font: ", e) 
img = Image.new('RGB', (640, 480), color = (73, 109, 137))
d = ImageDraw.Draw(img)
global userList
global userCount

import wsav
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
        elif id == 5: color = (255, 0, 0)       #Player btw
        elif id == 6: color = (0, 102, 204)

        #Renders object
        d.rectangle([(x, y), (x+16, y-16)], fill=color, outline=(0,0,0), width=0) 
    def delete(self, x, y):
        d.rectangle([(x, y), (x+16, y-16)], fill=(73, 109, 137), outline=(0,0,0), width=0)
    def draw(self, x, y, id):
        #Renders object
        color = None
        if id == 0: color = (73, 109, 137)
        elif id == 1: color = (97, 216, 0)
        elif id == 2: color = (147, 130, 50)
        elif id == 3: color = (94, 94, 93)
        elif id == 4: color = (38, 38, 38)
        elif id == 5: color = (255, 0, 0) #Player btw
        elif id == 6: color = (0, 102, 204)
        d.rectangle([(x, y), (x+16, y-16)], fill=color, outline=(0,0,0), width=0)

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 50, 40 # Size of the maximum amount of blocks in window (480p)
global world
world = [[block(0, f*16, 480-(h*16)) for f in range(w)] for g in range(h)]
# Spawn player
global player
player = block(block.player, 4*16, 480-((8*16)+1))

def spawnPlayer():
    global player
    player = block(block.player, 4*16, 480-((8*16)+1))


def GenerateWorld():
    # Generates a basic world

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

    spawnPlayer()
    print("e")



def PlayerControls(command):
    #fbb = world[int(player.x/16)][int(((480 - player.y)/16)-1)]
    #print(world[int(player.x/16)][int(((480 - player.y)/16)-1)].id)
    
    print("PlayerControls command: ", command)
    global player
    global InventoryID
    if command == "l":
        player.delete(player.x, player.y)
        player.x = player.x - 16
        player.draw(player.x, player.y, player.id)
    
    elif command == "r":
        player.delete(player.x, player.y)
        player.x = player.x + 16
        player.draw(player.x, player.y, 5)
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

        player.draw(player.x, player.y, 5); player.delete(player.x, player.y+16)

        world[int(player.x/16)][int(player.y/16)+1] = block(bbi, player.x, player.y+16)

    elif command == "d":
        
        player.y = player.y + 16
        player.draw(player.x, player.y, player.id)
        world[int(player.x/16)][int(player.y/16)] = block(0, player.x, player.y-16)
    elif command == "w":
        player.delete(player.x, player.y)
        player.y = player.y - 16
        player.draw(player.x, player.y, player.id)
    elif command == "i":
        if InventoryID == 3:
            InventoryID = 0
        else:
            InventoryID += 1
    else:
        return "Invalid command!"


userCount = 0
userList = [None]

def Render(user):
    global UserAlreadyExists
    UserAlreadyExists = False
    if userList[0] == None:
        userList[0] = user
    
    for x in userList:
        if x == user.split("#")[0]:
            UserAlreadyExists = True
            pass

    if UserAlreadyExists == False:
        print("Renderer.Render(): user appended -> ", user)
        userList.append(user)
    for x in range(len(userList)):
        d.text((10,50+(20*x)), "User: "+userList[x], fill=(255,255,0), font=font)
    #wsav.Save("save/world.save", world)
    img.save('imgrender/render.png')