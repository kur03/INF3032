import logging

class Logger() :
    
    def __init__(self) :
        logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")         #format how will the data be displayed in the file

    def info (self, message) :
        logging.info(message)
        
    def warning (self, message) :
        logging.warning(message)