import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt6.QtGui import QIcon, QFont    

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Commandes Morty')
        self.setWindowIcon(QIcon("img/robot_icon.ico"))
        self.label = QLabel('Choix du mode de connection', self)
        self.label.setFont(QFont('Arial', 20, QFont.Weight.Bold))
        self.label.move(100, 5)

        self.usbButton = QPushButton('USB', self)
        self.usbButton.setFont(QFont('Arial', 15, QFont.Weight.Bold))
        self.usbButton.resize(200, 150)
        self.usbButton.move(200, 50)
        self.usbButton.clicked.connect(self.on_click_usb)

        self.wifiButton = QPushButton('Wifi', self)
        self.wifiButton.setFont(QFont('Arial', 15, QFont.Weight.Bold))  
        self.wifiButton.resize(200, 150)
        self.wifiButton.move(200, 225)
        self.wifiButton.clicked.connect(self.on_click_wifi)
        self.show()

    def on_click_usb(self):
        print('Connection par USB')

    def on_click_wifi(self):
        print('Connection par Wifi')

    
def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


