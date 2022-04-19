from discord.ext import commands
import json, logging


class MyBot(commands.Bot) :
    
    def __init__(self) :
        super().__init__(command_prefix="!")
        self.remove_command("help")
        with open('config.json', 'r') as json_file:
            json_load = json.load(json_file)
        self.token = json_load["token"]
        
        
    async def on_ready(self):
        bot.load_extension("cogs.commandes")
        bot_channel = self.get_channel(961242684318683136)
        await bot_channel.send(f"JamesThePyBot is ready to help you !")
        logging.info("JamesThePyBot is ready to help you !")


if __name__ == "__main__" :
    
    logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")         #format how will the data be displayed in the file
    
    
    bot = MyBot()
    bot.run(bot.token)
