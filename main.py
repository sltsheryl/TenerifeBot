import discord
import os
from keep_alive import keep_alive
from weather.weather import get_weather
from help import help
from translate.translate import translate, get_languages
from quickmath.qmgame import add_score, get_question, get_score, reset, reply_ongoing, welcome_message
from quickmath.qmgame import reply_correct, reply_incorrect, switch_qm_ongoing, get_qm_status

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
    for command in help():
      lst += command + "\n"
    await message.channel.send("`{}`".format(lst))

  # WEATHER
  if message.content.startswith('~w'):
    city = message.content[slice(3, len(message.content))]
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


# QUICKMATH
# START
  if message.content == '~qm start' and not get_qm_status():
    switch_qm_ongoing()
    welcome = welcome_message()
    await message.channel.send(embed=welcome)
    while (True):
      generated = get_question()
      question = generated[0]
      answer = generated[1]
      await message.channel.send(question)

      user_answer = await client.wait_for(
        'message',
        check=lambda mess: mess.author != client and mess.channel == message.
        channel)

      # end game
      if user_answer.content == '~qm end':
        break

      # game already ongoing
      elif user_answer.content == '~qm start':
        ongoing = reply_ongoing()
        await message.channel.send(embed=ongoing)

      # correct
      elif (user_answer.content == str(answer)):
        player = user_answer.author.name
        add_score(player)
        correct_message = reply_correct()
        await message.channel.send(embed=correct_message)

      # incorrect
      else:
        incorrect_message = reply_incorrect()
        await message.channel.send(embed=incorrect_message)

    score_list = get_score()
    to_print = "Score 🎉" + '\n'
    for item in score_list:
      player_name = item[0]
      player_score = item[1]
      to_print += player_name + ": " + str(player_score) + '\n'
      reset()

    switch_qm_ongoing()
    await message.channel.send(to_print)

keep_alive()
client.run(os.getenv('TOKEN'))
