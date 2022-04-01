from discord import Client
from argparse import ArgumentParser
import json

class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")

    def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()
 
    def config():
        with open('json_data.json', 'r') as json_file:
            json_load = json.load(json_file)
        
        token = json_load["token"]    
        print(token)
