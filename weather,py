import requests, json
import os
import discord


def get_weather(city):
  try:
    base_url = "http://api.weatherapi.com/v1/current.json?key=" + os.getenv(
      'WEATHER_KEY')
    complete_url = base_url + "&q=" + city
    response = requests.get(complete_url)
    result = response.json()

    city = result['location']['name']
    country = result['location']['country']
    time = result['location']['localtime']
    wind_condition = result['current']['condition']['text']
    celcius = result['current']['temp_c']
    fahrenheit = result['current']['temp_f']
    fclike = result['current']['feelslike_c']
    fflike = result['current']['feelslike_f']

    embed = discord.Embed(title=f"{city}"
                          ' Weather',
                          description=f"{country}",
                          color=0x57ECF9)
    embed.add_field(name="Temperature C°", value=f"{celcius}", inline=True)
    # embed.add_field(name="Temperature F°", value=f"{fahrenheit}", inline=True)
    embed.add_field(name="Wind Conditions",
                    value=f"{wind_condition}",
                    inline=False)
    # embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
    embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
    embed.set_footer(text='Time: '
                     f"{time}")

    return embed
  except:
    embed = discord.Embed(title="No response", color=0xF34343)
    embed.add_field(name="Error",
                    value="Invalid input. Please enter a city name",
                    inline=True)
    return embed
