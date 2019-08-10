import discord
import search_mod
from discord import Webhook, RequestsWebhookAdapter


WEBHOOK_ID = 568630115974774863
WEBHOOK_TOKEN = 'sUxmT-o8siutqx64qWT8gSSKtka6xOHPxYzv80Y8188Jd8Ui_Aux2p888Q-_PU0Jcv-g'
client = discord.Client()
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

# WEBHOOK_ID2 = 569763783812317185
# WEBHOOK_TOKEN2 = '2030i39zOZRQ9E858VTjmBrU0kBQvCg9U7ReeUvSDYGFAnSOg-35lf5OHjlmq74icP01'
# webhook2 = Webhook.partial(WEBHOOK_ID2, WEBHOOK_TOKEN2, adapter=RequestsWebhookAdapter())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bot search '):
        embed = search_mod.search(message.content.replace('!bot search ', ''))
        webhook.send(embed=embed)
        # webhook2.send(embed=embed)
client.run('NDU5NTExMDI4OTM0Mzc3NDcy.XU1gug.mjWP4L2eg0cBCvqO6jYLS-bVTkk')
