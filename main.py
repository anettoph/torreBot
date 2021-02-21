import discord
import os 

client = discord.Client()

@client.event
async def on_ready():
	print("Hello! I'm {0.user}".format(client))

@client.event
async def on_messages(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))