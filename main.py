from keep_alive import keep_alive
from responses import responses
import discord
import os

client = discord.Client()
bot_token = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    word_list = message.content.split()
    choices = {'$help': 1, '$hello': 2}
    result = choices.get(word_list[0], 'default')

    await message.channel.send(responses.get(result, 'default'))


keep_alive()
client.run(bot_token)