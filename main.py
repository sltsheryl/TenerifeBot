import discord
import os
from keep_alive import keep_alive
from weather.weather import get_weather
from help import help
from translate.translate import translate, get_languages

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
    await message.channel.send(
      'Hello! Enter ~help to get the list of all the commands!')

  # ALL COMMANDS
  if message.content == '~help':
    lst = "Commands supported:" + "\n"
    for str in help():
      lst += str + "\n"
    await message.channel.send("`{}`".format(lst))

  # WEATHER
  if message.content.startswith('~w'):
    city = message.content[slice(9, len(message.content))]
    result = get_weather(city)
    await message.channel.send(embed=result)

  # LIST OF LANGUAGES
  if message.content.startswith('~t help'):
    lst = "Languages supported:" + "\n"
    for language in get_languages():
      lst += language + "\n"
    await message.channel.send("`{}`".format(lst))

  # TRANSLATE
  if message.content.startswith(
      '~t') and not message.content.startswith('~t help'):
    if len(message.content.split(' ')) < 3:
      await message.channel.send(
        "Invalid input. Enter ~help to see command formats")
    language = message.content.split(' ')[1]
    msg = ' '.join(message.content.split(' ')[2:])
    translated_message = translate(msg, language)
    if translated_message == "-1":
      await message.channel.send(
        "Invalid language. Enter ~t help to see languages supported!")
    else:
      await message.channel.send(translated_message)


keep_alive()
client.run(os.getenv('TOKEN'))
