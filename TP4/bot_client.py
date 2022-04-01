import discord
import json


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)



def config():
    with open('config.json', 'r') as json_file:
        json_load = json.load(json_file)
    
    return json_load["token"]

@client.event
async def on_ready():
    print("Le bot est prêt !")

#Il est important de mettre un paramètre dans on_message pour pouvoir récupérer le message, 
# sinon vous obtiendrez une erreur. 
@client.event
async def on_message(message):
    print(message.content)
    if message.content == "thank you":
        #Pour envoyer un message avec le bot, on utilise message.channel 
        # qui nous permet de récupérer le salon sur lequel le message a été envoyé. 
        # On utilise ensuite la méthode send de ce salon pour envoyer un message avec le bot.
        await message.channel.send("https://media.giphy.com/media/tXTqLBYNf0N7W/giphy.gif")
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
        
@client.event
async def on_member_join(member):
    general_channel = client.get_channel(959413124648271979)
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
    await general_channel.send(f"We've got a lost tourist here !")

token = config()
client.run(token)