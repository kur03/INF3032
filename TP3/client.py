from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys

class Main(QWidget):
    
    def __init__(self, hostname, api_key, ip):
        super().__init__()
        self.exe(hostname, api_key, ip)

    def exe(self, hostname, api_key, ip):

        #check for empty field
        if ((hostname == "") or (api_key == "") or (ip == "")):
            print("Error", "Empty field")
            sys.exit()
        
        else:
            url = hostname + "/ip/" + ip + "?key=" + api_key
            res = self.__query(url)
            lat = res["Latitude"]
            lon = res["Longitude"]
            if res:
                url_locate = QUrl("www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon) + ">#map=12")
                QDesktopServices.openUrl(url_locate)
                sys.exit()

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            print("Error", "IP not found")
            sys.exit()
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main(sys.argv[1], sys.argv[2], sys.argv[3])
    app.exec_() 
        
        