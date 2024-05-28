import sys

from application.connexion import *
from application.deplacement import *

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeyEvent
from application.connexion import connexion


class MartyRobotController(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.isControlTabActive = False

    def initUI(self):
        self.setWindowTitle("Marty Robot Controller")
        self.setGeometry(400, 400, 800, 600)
        self.setWindowIcon(QIcon("src/img/robot_icon.ico"))
        self.my_marty = None

        grid = QGridLayout()
        

        #create animated loading bar
        self.loadingBar = QProgressBar()
        self.loadingBar.setRange(0, 0)
        grid.addWidget(self.loadingBar, 1, 0, 1, 1)
        self.loadingBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loadingBar.hide()
        
        self.control_button = QPushButton("Control")
        self.control_button.setStyleSheet("""
            QPushButton {
            background-color: red;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            width: 200px;
            font-size: 20px;
            font-weight: bold;
            }
        """)
        self.control_button.clicked.connect(self.controlClicked)
        self.control_button.hide()

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
        grid.addWidget(self.control_button, 0, 0, 1, 1)
        

        self.setLayout(grid)

    def usbClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.loadingScreen.show()
        self.loadingBar.show()
        (connecter, my_marty)=connexion(False)
        if(connecter):
            print("Le robot est connecté")
            self.my_marty = my_marty

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
        if self.ipAddress.text() == "":
            (connecter,my_marty)=connexion(True)
            if (connecter):
                print("le robot est connecté")
                self.my_marty = my_marty
        else:
            (connecter,my_marty)=connexion(True, self.ipAddress.text())
            if (connecter):
                print("le robot est connecté")
                self.my_marty = my_marty
            
    def getMyMarty(self):
        return self.my_marty

    def homeClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.homeButton.hide()
        self.usbButton.show()
        self.wifiButton.show()
        self.mainTitle.show()
        self.control_button.show()
        self.isControlTabActive = False
        
    def controlClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.control_button.show()
        self.homeButton.show()
        self.my_marty = self.getMyMarty()
        if self.my_marty is not None:
            self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            self.setFocus()
            self.isControlTabActive = True
        else:
            print("No marty object available")
            self.homeClicked()

    def keyPressEvent(self, event):
        if self.isControlTabActive:
            if self.my_marty is not None:
                if event.key() == Qt.Key.Key_Z:
                    movementDirection(self.my_marty,"forward")
                    print("walking forward")
                elif event.key() == Qt.Key.Key_S:
                    movementDirection(self.my_marty,"backwards")
                    print("walking backward")
                elif event.key() == Qt.Key.Key_Q:
                    movementDirection(self.my_marty,"left")
                    print("turning left")
                elif event.key() == Qt.Key.Key_D:
                    movementDirection(self.my_marty,"right")
                    print("turning right")
                elif event.key() == Qt.Key.Key_1:
                    self.my_marty.celebrate()
                    print("celebration in progress !")
                elif event.key() == Qt.Key.Key_2:
                    self.my_marty.dance()
                    print("dancing in progress !")
                elif event.key() == Qt.Key.Key_Escape:
                    self.my_marty.stop()
                    print("stopping")
                else:
                    print("Key not recognized")
            else:
                print("No marty object available")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MartyRobotController()
    controller.show()
    sys.exit(app.exec())