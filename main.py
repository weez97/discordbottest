import os
import re
import discord
from keep_alive import keep_alive

client = discord.Client()
bot_token = os.environ['TOKEN']

def options(selected):
  choices = {'$help': display_help(), '$hola': 1}
  result = choices.get(selected, 'default')
  return result

def purge_messages():
  x = 0

def display_help():
  print(f'bonito esta python')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    word_list = message.content.split()
    result = options(word_list[0])


    #await message.channel.send(result)

keep_alive()
client.run(bot_token)