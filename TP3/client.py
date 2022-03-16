"""     Exercise n°5
import requests
from PyQt5.QtWidgets import QMessageBox

class Main():
    def query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":

    main = Main()
    hostname="127.0.0.1:8000"
    res = main.query(hostname)
    if res:
        print(res)
"""

"""     Exercise n°6 """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Customer")
        self.setFixedSize(400, 400)
        
        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(10, 0)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)
        
        self.label2 = QLabel("Enter your API key:", self)
        self.label2.move(10, 60)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 90)
        
        self.label3 = QLabel("Enter your IP:", self)
        self.label3.move(10, 120)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 150)
        
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 180)
        
        self.button = QPushButton("Send", self)
        self.button.move(10, 210)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text1.text()
        api_key = self.text2.text()
        ip = self.text3.text()

        #check for empty field
        if ((hostname == "") or (api_key == "") or (ip == "")):
            QMessageBox.about(self, "Error", "Please fill the field")
        
        else:
            url = hostname + "/ip/" + ip + "?key=" + api_key
            res = self.__query(url)
            lat = res["Latitude"]
            lon = res["Longitude"]
            if res:
                self.label4.setText("Longitute: %s\nLatitude: %s " % (lon, lat))
                self.label4.adjustSize()
                self.show()
                url_locate = QUrl("www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon) + ">#map=12")
                QDesktopServices.openUrl(url_locate)

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
        
        