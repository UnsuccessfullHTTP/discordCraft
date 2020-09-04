#
# PYTHON CONSOLE DESINGED FOR DISCORDCRAFT BOT BY UNSUCCESFULHTTP
#
# Execute python code while its running!
#

async def console_begin():
    print("--------")
    print("Python console by UnsuccesfulHttp")
    print("Execute console_help() without for help!")
    print("WARNING: This could break the bot if misused, please use with caution")
    print("--------")
    await console_input()
    
async def console_input():
    cmdinput3434 = input("CONSOLE:> ")
    await console_exec(cmdinput3434)
    
    
async def console_exec(input):
    try:
        exec(input)
    except Exception as e:
        print("Console exception: ", e)
    await console_input()
        
async def console_help():
    print("Console help: Comming soon!")
    await console_input()
    