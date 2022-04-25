from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys

class Main():
    
    def __init__(self, hostname, key, ip):
        self.hostname = hostname
        self.api_key = key
        self.ip = ip

    def exe(self):

        #check for empty field
        if ((self.hostname == "") or (self.api_key == "") or (self.ip == "")):
            print("Error", "Empty field")
            sys.exit()
        
        else:
            url = self.hostname + "/ip/" + self.ip + "?key=" + self.api_key
            res = self.__query(url)
            lat = res["Latitude"]
            lon = res["Longitude"]
            if res:
                return "www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon) + ">#map=12"
        
                

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            print("Error", "IP not found")
            sys.exit()
        if r.status_code == requests.codes.OK:
            return r.json()


def client(host, key, ip) :
    main = Main(host, key, ip)
    url = main.exe()
    return url      
        