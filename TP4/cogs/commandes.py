import discord
from discord.ext import commands
from shiritori import shiritori


class MyCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="What can James do for you ?", url="", description="This is a manual on how to use James", color=0xFF5733)
        
        embed.set_author(name="Chloé", url="https://github.com/kur03")
        
        embed.add_field(name="Real commands", value="These are the commands you can use with the prefix !.", inline=False)
        embed.add_field(name="!help", value="Sends this message.", inline=True)
        embed.add_field(name="!del", value="As you guessed it ~~adds~~ delete the message. Add the number of message.", inline=True)
        
        embed.add_field(name="Not real commands", value="These are the commands you can use with the prefix !.", inline=False)
        embed.add_field(name="gperdu", value="Display a little 'I Lost' picture.", inline=True)
        
        embed.add_field(name="Games", value="These are the commands you can use with the prefix !.", inline=False)
        embed.add_field(name="shiritoi", value="Check and save words used in the shiritori.", inline=True)
        
        embed.set_footer(text="For any question @kuroe#4981")
        
        await ctx.send(embed=embed)
        
        
    @commands.command(name="del")
    async def delete(self, ctx, number: int):
        messages = await ctx.channel.history(limit=number + 1).flatten()
        
        for each_message in messages:
            await each_message.delete()
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "gperdu":
            #Pour envoyer un message avec le bot, on utilise message.channel 
            # qui nous permet de récupérer le salon sur lequel le message a été envoyé. 
            # On utilise ensuite la méthode send de ce salon pour envoyer un message avec le bot.
            await message.channel.send("https://cdn.discordapp.com/attachments/760200285498376212/958278241314025532/sipersicret.png")           

        if message.channel.name == "🐍-tp4" :
            if message.author.name != "JamesThePyBot" :    
                if shiritori(message.content) :
                    await message.channel.send(f"{message.author.mention} ce mot a déjà été utilisé tu as donc perdu. Tu pourras recommencer à jouer au prochain tour !")
                    
           
              
    async def on_member_join(self, member):
        general_channel = self.client.get_channel(959413124648271979)
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
        await general_channel.send(f"We've got a lost tourist here !")
    
        
        
def setup(bot):
    bot.add_cog(MyCommands(bot))