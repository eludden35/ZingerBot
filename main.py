import discord
import os

THRESHOLD = 10

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_server_join(server):
    return await client.send_message(
    server.default_channel,
    """ 📌 I pin the funniest shit. 📌 """
    )

@client.event
async def on_reaction_add(reaction, user):
    if reaction.count >= THRESHOLD:
        print(reaction.message.content)
        await reaction.message.pin()

client.run(os.getenv('TOKEN'))