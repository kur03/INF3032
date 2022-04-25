from discord.ext import commands
import json
from logger import Logger


class MyBot(commands.Bot) :
    
    def __init__(self, log) :
        super().__init__(command_prefix="!")
        self.remove_command("help")
        with open('config.json', 'r') as json_file:
            json_load = json.load(json_file)
        self.token = json_load["token"]
        self.log = log
        
        
    async def on_ready(self):
        bot.load_extension("cogs.commandes")
        bot_channel = self.get_channel(961242684318683136)
        await bot_channel.send(f"JamesThePyBot is ready to help you !")
        self.log.info("JamesThePyBot is ready to help you !")


if __name__ == "__main__" :
    
    log = Logger()
    bot = MyBot(log)
    bot.run(bot.token)
