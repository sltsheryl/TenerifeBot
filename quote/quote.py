import requests, json
import os
import discord

QUOTES_API_URL = "https://api.api-ninjas.com/v1/quotes?category=love"


def get_quote():
  response = requests.get(QUOTES_API_URL,
                          headers={'X-Api-Key': os.getenv('QUOTE_KEY')})
  if response.status_code == 200:
    data = response.json()
    quote = data[0]['quote']
    return quote
  else:
    return 'Error: Could not retrieve quote!'
