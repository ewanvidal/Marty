import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from application.connexion import connexion


class MartyRobotController(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Marty Robot Controller")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowIcon(QIcon("src/img/robot_icon.ico"))

        grid = QGridLayout()

        #create animated loading bar
        self.loadingBar = QProgressBar()
        self.loadingBar.setRange(0, 0)
        grid.addWidget(self.loadingBar, 1, 0, 1, 1)
        self.loadingBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loadingBar.hide()
        

        #create loading screen
        self.loadingScreen = QLabel()
        self.loadingScreen.setText("Loading...")
        self.loadingScreen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loadingScreen.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
            }
        """)
        grid.addWidget(self.loadingScreen, 1, 0, 1, 2)
        self.loadingScreen.hide()

        #create input for IP address
        self.ipAddress = QLineEdit()
        self.ipAddress.setPlaceholderText("Enter IP Address")
        self.ipAddress.setMaxLength(15)
        self.ipAddress.setStyleSheet("""
            QLineEdit {
                border: 2px solid #0047AB;
                border-radius: 5px;
                padding: 10px;
                font-size: 20px;
            }
        """)
        self.ipAddress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.ipAddress, 1, 1, 1, 1)
        self.ipAddress.hide()
        
        # Style the home button
        self.homeButton = QPushButton("Home")
        self.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                width: 50px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.homeButton.hide()
        self.homeButton.clicked.connect(self.homeClicked)
        
        self.mainTitle = QLabel("Marty Robot Controller")
        self.mainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainTitle.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 40px;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
            }
        """)
        
        # Style the USB button
        self.usbButton = QPushButton("USB")
        self.usbButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                height: 50px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.usbButton.clicked.connect(self.usbClicked)
        
        self.wifiButton = QPushButton("WiFi")
        self.wifiButton.setStyleSheet("""
            QPushButton {
                background-color: #0047AB;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                height: 50px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.wifiButton.clicked.connect(self.wifiClicked)
        
        
        grid.addWidget(self.mainTitle, 1, 0, 1, 2)
        grid.addWidget(self.homeButton, 0, 1, 1, 1)
        grid.addWidget(self.usbButton, 2, 0, 1, 1)
        grid.addWidget(self.wifiButton, 2, 1, 1, 1)   

        self.setLayout(grid)

    def usbClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.loadingScreen.show()
        self.loadingBar.show()
        connexion(False)
        

    def wifiClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.ipAddress.show()
        self.homeButton.show()
        self.ipAddress.returnPressed.connect(self.onReturnPressed)
        
        
    def onReturnPressed(self):
        connexion(True, self.ipAddress.text())
        
    def homeClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.homeButton.show()
        self.usbButton.show()
        self.wifiButton.show()
        self.mainTitle.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MartyRobotController()
    controller.show()
    sys.exit(app.exec())