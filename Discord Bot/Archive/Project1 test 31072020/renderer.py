
from PIL import Image, ImageDraw, ImageFont



# Initialization
global InventoryID
InventoryID = 0
font = ImageFont.truetype("FFFFORWA.TTF", 10)
img = Image.new('RGB', (640, 480), color = (73, 109, 137))
d = ImageDraw.Draw(img)
global userList
global userCount



#
# TERRAIN GENERATION V1
# 
# DESCRIPTION: 
# Basic superflat world
# 
# GENERATION block (y coord):
# AIR 8+
# GRASS 7
# DIRT 6 - 4
# STONE 3 - 1
# BEDROCK 1
#
# BLOCK ID:
# AIR       0
# GRASS     1
# DIRT      2
# STONE     3
# BEDROCK   4
# PLAYER    5   (Internaly counts as a block)
# 
#  


# Makes a block
 
class block:
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
        elif id == 5: color = (255, 0, 0) #Player btw

        #Renders object
        d.rectangle([(x, y), (x+16, y-16)], fill=color, outline=(0,0,0), width=0) 
    def delete(self, x, y):
        d.rectangle([(x, y), (x+16, y-16)], fill=(73, 109, 137), outline=(0,0,0), width=0)
    def draw(self, x, y):
        #Renders object
        d.rectangle([(x, y), (x+16, y-16)], fill=(255, 0, 0), outline=(0,0,0), width=0)

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 410, 310 # Size of the maximum amount of blocks in window (480p)
world = [[block(0, -100, -100) for f in range(w)] for g in range(h)]

def GenerateWorld():
    # Generates a basic world


    # Fixed text that displays current version 
    d.text((10,10), "Project1 test 31072020", fill=(255,255,0), font=font)

    # Generates grass
    for x in range(40):
        world[x][7] = block(1, x*16, 480-(7*16))

    # Generates dirt
    for x in range(40):
        world[x][6] = block(2, x*16, 480-(6*16))
    for x in range(40):
        world[x][5] = block(2, x*16, 480-(5*16))
    for x in range(40):
        world[x][4] = block(2, x*16, 480-(4*16))

    # Generates stone
    for x in range(40):
        world[x][3] = block(3, x*16, 480-(3*16))
    for x in range(40):
        world[x][2] = block(3, x*16, 480-(2*16))
    for x in range(40):
        world[x][1] = block(3, x*16, 480-(1*16))

    # Generates bedrock
    for x in range(40):
        world[x][0] = block(4, x*16, 480-(0*16))

    # Spawn player
    global player
    player = block(5, 4*16, 480-((8*16)+1))



def PlayerControls(command):
    #fbb = world[int(player.x/16)][int(((480 - player.y)/16)-1)]
    
    global InventoryID
    if command == "l":
        player.delete(player.x, player.y)
        player.x = player.x - 16
        player.draw(player.x, player.y)
    elif command == "r":
        player.delete(player.x, player.y)
        player.x = player.x + 16
        player.draw(player.x, player.y)
    elif command == "b":
        if InventoryID == 0:
            bbi = 3
        elif InventoryID == 1:
            bbi = 2
        elif InventoryID == 2:
            bbi = 1
        world[int(player.x/16)][int(player.y/16)] = block(bbi, player.x, player.y)
        player.y = player.y - 16
        player.draw(player.x, player.y)
    elif command == "d":
        world[int(player.x/16)][int(player.y/16)] = block(0, player.x, player.y)
        player.y = player.y + 16
        player.draw(player.x, player.y)
    elif command == "w":
        player.delete(player.x, player.y)
        player.y = player.y - 16
        player.draw(player.x, player.y)
    elif command == "i":
        if InventoryID == 2:
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
        if x == user:
            UserAlreadyExists = True
            pass

    if UserAlreadyExists == False:
        userList.append(user)
    for x in range(len(userList)):
        d.text((10,50+(20*x)), "User: "+userList[x], fill=(255,255,0), font=font)
    img.save('imgrender/render.png')