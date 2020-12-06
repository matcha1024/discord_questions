import discord
import random

client = discord.Client()
token = "xxxxxxxxxxxxxx..."

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

q = []
@client.event
async def on_message(message):
    global q
    if message.author.bot:
        return
    elif message.content.startswith('qadd'):
        q.append(message.content[5:])
        await message.add_reaction('👍')
    elif message.content == 'qrand':
        if(len(q) == 0):
            await message.channel.send('問題がありません。')
        else:
            await message.channel.send(random.choice(q))
    elif message.content == 'qclear':
        q = []
        await message.channel.send('初期化しました。')
    elif message.content == 'qqueue':
        await message.channel.send(q)
    elif message.content.startswith('qrem'):
        num = int(message.content[5:])
        q.pop(num - 1)
        await message.add_reaction('👍')


client.run(token)
