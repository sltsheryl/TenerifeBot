import discord
import os
from keep_alive import keep_alive
from weather import get_weather

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == '~hello':
    await message.channel.send('Hello! Enter ~help to get the list of all the commands!')

  if message.content.startswith('~weather'): 
    city = message.content[slice(9, len(message.content))]
    print(city)
    result = get_weather(city)
    await message.channel.send(embed=result)


keep_alive()
client.run(os.getenv('TOKEN'))
