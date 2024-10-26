# This example requires the 'message_content' intent.

import discord, logging, tweepy
import tweepy.client

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

consumer_key = '$X_API_KEY' #API Key
consumer_secret = '$X_API_KEY_SECRT' #API Key Secret
access_token = '$X_TOKEN'
access_token_secret = '$X_TOKEN_SECRET'

xClient = tweepy.client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run("'$BOT_TOKEN'", log_handler=handler, log_level=logging.DEBUG)