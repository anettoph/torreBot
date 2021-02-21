import discord
import os 
import requests
import json

client = discord.Client()

def get_quote():
	response = requests.get


@client.event
async def on_ready():
	print("Hello! I'm {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))