import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send('Some Inspiration:')
    await message.channel.send(quote)

  elif message.content.startswith('$'):
    await message.channel.send('That went over my head!')

  elif message.content.startswith('Hey You'):
    await message.channel.send('How are you ' + str(message.author) +'?')

client.run(os.getenv('TOKEN'))
