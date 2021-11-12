# Import
import requests
import datetime
import asyncio
import discord
import json
import os 

# From
from discord.ext import commands
from bs4 import BeautifulSoup
from pathlib import Path 

# Variable
URL = "https://prepareyourwallet.com/"
Headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
	} 

# Class
class General(commands.Cog):
	def __init__(self, bot):

		# Variable
		self.bot = bot 

	# On Message
	@commands.Cog.listener()
	async def on_message(self, ctx):

		# Variable
		r = requests.get(URL, headers=Headers)
		soup = BeautifulSoup(r.content, "lxml")

		sale_name = soup.find("h2", attrs={'class': 'h5 mb-3 text-white'}).text
		start_date = soup.find("span", attrs={'itemprop': 'startDate'}).text
		end_date = soup.find("span", attrs={'itemprop': 'endDate'}).text
		count_down = soup.find('span', attrs={'id': 'countdown'}).text
		status = soup.find('span', attrs={'class': "status mb-0 mt-2 float-lg-right"}).text
        
        
		if self.bot.user.mentioned_in(ctx):
		    await ctx.add_reaction('✅')
		    await ctx.author.send(f'**__ # When is the new Steam sale?__**\n\n **🏷️️ {sale_name}** \n\n**📅 {start_date} |  {end_date}** \n\n**⏰ {count_down}** \n\n**📌 {status}**')
		    
		    # Embed
		    e = discord.Embed(
		    	title='Prepare Your Wallet',
		    	url=URL
		    )
		    e.set_author(name='Data Source:')
		    
		    await ctx.author.send(embed=e)
		    
			
# Setup 
def setup(bot):
	bot.add_cog(General(bot))
		

