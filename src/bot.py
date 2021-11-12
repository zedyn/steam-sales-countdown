# Import
import discord
import json
import os 

# From
from discord.ext import commands
from pathlib import Path

# CWD
cwd = Path(__file__).parents[0]
cwd = str(cwd)

# Secret File
secret_file = json.load(open(cwd + '/database/secret_file.json'))

# Class
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned, help_command=None)
        
        
    # On Ready
    async def on_ready(self):
        # Log
        print('Loading...')

        # Extension Loader
        try:
            self.load_extension('commands.general')
            
            #Log
            print('Complated')
            
            # Change Presence
            await self.change_presence(activity=discord.Game(name='Mention me!'))
            
            # Log
            print('Bot\'s ready with all functions!')
            print('Developed by zédyN.')
            print('https://github.com/zedyn')
              
        except Exception as e:
            # Log
            print('Error! \n{}'.format(e))
		            
		            
		            
bot = Bot()
bot.run(secret_file['bot_token'])       
    
           