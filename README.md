# Discord Craft by UnsuccessfulHTTP
# Important
### **Please read this before installing**
## About
This is a 2D inspired version of minecraft ported to a discord bot
#### Stable release: `v0.1 Pre-Alpha` `Version number: 3`
#### WIP release: `v0.2 Pre-alpha` `Version number: WIP4`
## How to set up
1. ### First clone the repository and unzip it

  - **If you want a somewhat stable version of Discord Craft download the latest release**
	  - In the github repository click in releases the latest one
	  - Download the source code from there
  - **If you want the latest commit (Highly unstable)**
	  - Download the repository from the github page


2. ### Create a discord bot

 - [Open the discord developer portal](https://discord.com/developers/applications "Open the discord developer portal") (You first need a discord account)
 - Make a new application
 - Open the application and make a new bot on the `Bot` tab
 - Go to the `OAuth2` tab
 - Scroll down to `OAuth2 link generator`
 - Select `bot` in scopes
 - Select `administrator`in permissions
 - Copy the link and open it in a new tab and add it to a server you own
 - Go back to your new application and go to the `Bot` tab
 - Copy the token
 	- **IMPORTANT:** This token is used to control your bot, as so, treat it like a password
		- **If you suspect that someone has your token, click `Regenerate` to replace yout old token**


3. ### Create an environment variable called `DiscordCraftBotToken` where the value will be your discord bot token (Not supported in `v0.1 Pre Alpha release`)
 - #### v0.2 Pre-Alpha

      - Windows

    		- Open the classic `Control Panel.`
    		- Navigate to `Control Panel\User Accounts\User Accounts.`
    		- On the left, click on the `Change my environment variables link`
    		- Click `Add`
    		- In the `Name` field write `DiscordCraftBotToken` and in the `Value` field copy/paste your bot token
 
 		- Mac OS
    		- Open terminal
			- Run the command `nano ~/.bash_profile`
			- Add a line saying `export DiscordCraftBotToken=[YOUR BOT TOKEN HERE]`
			- Hit `Ctrl+o`, `enter` and `Ctrl+x` to save and exit

 		- Linux
 
 			- Open terminal
 			- Run the command `nano /etc/environment`

			- Add a line saying `export DiscordCraftBotToken=[YOUR BOT TOKEN HERE]`
			- Hit `Ctrl+o`, `enter` and `Ctrl+x` to save and exit


 - #### v0.1 Pre-Alpha

 - Open the unzipped file and enter the `Discord Craft` folder
 - Open the `token` folder
 - Edit the `bot_token.txt` file with a text editor
 - Replace the bot token with yours (Default token doesn´t work)
 - Save and exit

4. ### Install python 3.7+ (It will not run on older versions)

 - Download page of python with instructions (automatically detects your operating system): https://www.python.org/downloads/
 - This tutorial covers in-depth the installation process for the 3 main operating systems: https://realpython.com/installing-python/
 

5. ### In the command line run `pip install discord` to install the discord api

6. ### In the command line run `pip install pillow` to install the image engine
7. ### Configure the bot to use the server

	- Enable developer mode in discord
		- Go to your discord settings
		- Go to `Appereance`
		- Scroll down to `Advanced`
		- Enable developer mode
	- Go to your discord server in which you added the bot
	- Right click the channel in which the bot will interact and select `Copy ID`
		- **NOTE:** It is recommended to do a dedicated channel since this bot spams a lot (Im working on fixing it)
	- Go where you installed the bot and enter the `Discord Craft` folder
	- Open `config.ini`with any text editor
	- change the channel variable with the ID you copied
		- It should look like this `channel=123456789`
	- Save and exit


8. ### Open the folder called `DiscordCraft` and run `run.bat`(Windows) or open the folder in a command line and run `python3 main.py` (Multi-system)


# Internal structure

## Discord Craft Folder
### Main.py
The main part of the bot. It handles the human/bot interactions as well as the main driver for the discord.py api
### Config.ini
The general configurations of the bot
## Discord Craft / lib  Folder
### Renderer.py
The main logic part of the bot. It handles almost all the internal logic along with the image logic.
### Wsav.py
Mini driver used for saving/loading logic with Pickle

# Using the bot

## After installation

After you successfully install and run the bot it should send a message that says 
> Bot is ready!

This means that the bot is ready to use 
## Controls

**Format:** Command name (Reaction) (text command)

- Render (Counter-clockwise)(render)
	- Used for generating a new world
- Left (Left arrow)(l)
	- Move the player to the left
- Right (Right arrow)(r)
	- Move the player to the right
- Up (Up arrow)(w)
	- Move the player up
- Destroy (Hammer)(d)
	- Destroy the block bellow and move down
- Build (Wrench)(b)
	- Build the selected block and move up
- Inventory toggle (Box)(i)
	- The inventory is 4 different blocks
	- When you inventory toggle you select the next one on the inventory
	- **Example:**
		- A **B** C
		- A B **C**
		- **A** B C
- Save (Floppy disk)(save)
	- Saves the world to `Discord Craft/save/world.save`
- Load (Inbox)(fload)
	- Loads the world from `Discord Craft/save/world.save`


# Privacy warning
---
This bot logs all controls that have been fed (like up, build, etc...), username of the sender, and time of sending, the message (With its effects like activating PlayerControls). This information is all visible from the command line of which you ran the command. Please have this in mind when using this bot. I am working to add a disabling feature to these logs.

- Example of actual starting logs:
	`D:\GitHub\discordCraft\Discord Bot>python main.py`
	`------------`
	`UnsuccesfulHttp DiscordCraft made in July 2020 - August 2020`
	`Current game version: DiscordCraft Pre-alpha v0.2`
	`Bot program started!    Tue Sep 22 12:22:56 2020`
	`------------`

	`Bot is ready    Tue Sep 22 12:22:59 2020`

	`------------`
	`Message detected: User: DiscordCraft DevBot#0343 Contents:  Time:     Tue Sep 22 12:22:59 2020`
	`Reaction added! User: DiscordCraft DevBot#0343 Emoji: 🔄  Time:    Tue Sep 22 12:23:00 2020`
# Support

Do you have any questions about the bot or need support?
Feel free to contact me:

Email: **unsuccesfulhttp@protonmail.com**

Discord: **UnsuccessfulHTTP#0239**

Try the bot: **https://discord.gg/6Z2z7zx** 