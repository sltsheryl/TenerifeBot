from quickmath.Expression import Expression
import discord
import cexprtk
import math

status_ongoing = False
score = {}


def switch_qm_ongoing():
  global status_ongoing
  if status_ongoing:
    status_ongoing = False
  else:
    status_ongoing = True


def get_qm_status():
  return status_ongoing


def get_question():
  qn = str(Expression(4, None, 0))
  ans = math.trunc(cexprtk.evaluate_expression(qn, {}))
  return (qn, ans)


def get_score():
  print(score.items())
  return list(score.items())


def add_score(player):
  if player not in score:
    score[player] = 1
  else:
    score[player] += 1


def welcome_message():
  embed = discord.Embed(
    title='Quickmath',
    description=
    "Welcome to QuickMath! Answer as many questions as you can! Type ~qm end to end the game.",
    color=0x9E59CC)
  return embed


def reset():
  score.clear()


def reply_ongoing():
  embed = discord.Embed(title='Quickmath',
                        description="Game ongoing!",
                        color=0xfcd703)
  return embed


def reply_correct():
  embed = discord.Embed(title='Quickmath',
                        description="Correct",
                        color=0x50C878)
  return embed


def reply_incorrect():
  embed = discord.Embed(title='Quickmath',
                        description="Incorrect",
                        color=0xFF5733)
  return embed
