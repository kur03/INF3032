import discord, logging
from discord.ext import commands
from shiritori import shiritori
from web.client import client
import logger

class MyCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def help(self, ctx):
        logging.info("Display command manual")
        embed=discord.Embed(title="What can James do for you ?", url="", description="This is a manual on how to use James", color=0xFF5733)
        
        embed.set_author(name="Chloé", url="https://github.com/kur03")
        
        embed.add_field(name = chr(173), value = chr(173))
        embed.add_field(name="Real commands", value="These are the commands you can use with the prefix !.", inline=False)
        embed.add_field(name="!help", value="Sends this message.", inline=False)
        embed.add_field(name="!del", value="As you guessed it ~~adds~~ delete the message. Add the number of message.", inline=False)
        embed.add_field(name="!map", value="Gives the link toward a map of the pysical adress of an ip adress. Add the host name, your shodan key and the ip adress.", inline=False)
        embed.add_field(name="!happydance", value="Display and dancing gif. To use when you finally fix a bug or achieve something you're pround of.", inline=False)
        
        embed.add_field(name = chr(173), value = chr(173))
        embed.add_field(name="Not real commands", value="These are the commands you can use with the prefix !.", inline=False)
        embed.add_field(name="gperdu", value="Display a little 'I Lost' picture.", inline=True)
        
        embed.set_footer(text="For any question @kuroe#4981")
        
        await ctx.send(embed=embed)
        
        
    @commands.command(name="del")
    async def delete(self, ctx, number: int):
        self.bot.log.info(f"{number} messages were deleted")
        messages = await ctx.channel.history(limit=number + 1).flatten()
        
        for each_message in messages:
            await each_message.delete()
            
            
    @commands.command(name="map")
    async def give_map(self, ctx, host, key, ip) :
        url = client(host, key, ip)
        self.bot.log.info(f"Reaching webserver")
        await ctx.channel.send(f"{url}!")
        
        
    @commands.command(name="happydance")
    async def dance_gif(self,ctx) :
        self.bot.log.info(f"Sending gif")
        await ctx.channel.send(f"https://media.giphy.com/media/cFSbwZr4i0hVe/giphy.gif")
    
    
    @commands.Cog.listener()   
    async def on_member_join(self, member):
        self.bot.log.info(f"{member.display_name} has join the server !")
        general_channel = self.client.get_channel(959413124648271979)
        await general_channel.send(f"Welcome {member.display_name} !")
    
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "gperdu" :
            #Pour envoyer un message avec le bot, on utilise message.channel 
            # qui nous permet de récupérer le salon sur lequel le message a été envoyé. 
            # On utilise ensuite la méthode send de ce salon pour envoyer un message avec le bot.
            await message.channel.send("https://cdn.discordapp.com/attachments/760200285498376212/958278241314025532/sipersicret.png")
            self.bot.log.info(f"Message sent in {message.channel}")

        if message.author.name != "JamesThePyBot" and message.channel.name == "🧬-shiritori" :    
            if shiritori(message.content) :
                await message.channel.send(f"{message.author.mention} ce mot a déjà été utilisé tu as donc perdu. Tu pourras recommencer à jouer au prochain tour !")
                self.bot.log.info(f"{message.author.name} has lost")
              
    
def setup(bot):
    bot.add_cog(MyCommands(bot))