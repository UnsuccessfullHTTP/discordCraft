# Discord Craft
Developed by UnsuccessfulHTTP
## About
This is a 2D inspired version of minecraft ported to a discord bot
#### Stable release: `v0.1 Pre-Alpha` `Version number: 3`
#### WIP release: `v0.2 Pre-alpha` `Version number: 4`
## How to set up
1. First clone the repository and unzip it

  - If you want a somewhat stable version of Discord Craft download the `v0.1 Pre Alpha release` or if you want to download the latest version (Not recommended) just click the download button to download the zip
   
   
3. Create an enviroment variable called `DiscordCraftBotToken` where the value will be your discord bot token (Not supported in `v0.1 Pre Alpha release`)
- v0.2 Pre-Alpha

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
	
	
- v0.1 Pre-Alpha

 - Open the unzipped file and enter the `Discord Craft` folder
 - Open the `token` folder
 - Edit the `bot_token.txt` file with a text editor
 - Replace the bot token with yours (Default token doesn´t work)
 - Save and exit

4. Install python 3.7+ (It will not run on older versions)

 - This tutorial covers in-depth the installation process for the 3 main operating systems: https://realpython.com/installing-python/

4. In the command line run `pip install discord` to install the discord api
5. In the command line run `pip install pillow` to install the image engine
6. Open the folder called `DiscordCraft` and run `run.bat`(Windows) or open the folder in a command line and run `python3 main.py` (Multi-system) in a command line and run `python3 main.py`