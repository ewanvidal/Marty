import sys

from application.connexion import *
from application.deplacement import *

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeyEvent
from application.connexion import connexion
from application.labyrinthe import labyrintheColor
from application.Calibrage import Calibrage


class MartyRobotController(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.isControlled = False
        
        #create background
        self.setStyleSheet("""
            QLabel {
                background-image: url('src/img/background.jpg');
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)
        

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
        
        #create calibration button
        self.calibrationButton = QPushButton("Calibrate")
        self.calibrationButton.setStyleSheet("""
            QPushButton {
            background-image: url('src/img/ainbow_gradient.jpg');
            background-repeat: no-repeat;
            background-position: center;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            width: 200px;
            font-size: 20px;
            font-weight: bold;
            }
        """)
        self.calibrationButton.clicked.connect(self.calibrationClicked)
        self.calibrationButton.hide()
        
        #create red, green, blue, light blue, yellow, pink, black buttons
        self.redButton = QPushButton("Red")
        self.redButton.setStyleSheet("""
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
        self.redButton.clicked.connect(self.redClicked)
        self.redButton.hide()
        
        self.greenButton = QPushButton("Green")
        self.greenButton.setStyleSheet("""
            QPushButton {
                background-color: green;    
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.greenButton.clicked.connect(self.greenClicked)
        self.greenButton.hide()
        
        self.blueButton = QPushButton("Blue")
        self.blueButton.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.blueButton.clicked.connect(self.blueClicked)
        self.blueButton.hide()
        
        self.lightBlueButton = QPushButton("Light Blue")
        self.lightBlueButton.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.lightBlueButton.clicked.connect(self.lightBlueClicked)
        self.lightBlueButton.hide()
        
        self.yellowButton = QPushButton("Yellow")
        self.yellowButton.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.yellowButton.clicked.connect(self.yellowClicked)
        self.yellowButton.hide()
        
        self.pinkButton = QPushButton("Pink")
        self.pinkButton.setStyleSheet("""
            QPushButton {
                background-color: pink;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.pinkButton.clicked.connect(self.pinkClicked)
        self.pinkButton.hide()
        
        self.blackButton = QPushButton("Black")
        self.blackButton.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.blackButton.clicked.connect(self.blackClicked)
        self.blackButton.hide()

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
        grid.addWidget(self.calibrationButton, 0, 1, 1, 1)
        
        grid.addWidget(self.redButton, 0, 0, 1, 1)
        grid.addWidget(self.greenButton, 0, 1, 1, 1)
        grid.addWidget(self.blueButton, 1, 0, 1, 1)
        grid.addWidget(self.lightBlueButton, 1, 1, 1, 1)
        grid.addWidget(self.yellowButton, 2, 0, 1, 1)
        grid.addWidget(self.pinkButton, 2, 1, 1, 1)
        grid.addWidget(self.blackButton, 3, 0, 1, 1)

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
            self.my_marty.play_mp3("sounds/Connect.mp3")
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
                #self.my_marty.play_mp3("src\sounds\Connect.mp3")
        else:
            (connecter,my_marty)=connexion(True, self.ipAddress.text())
            if (connecter):
                print("le robot est connecté")
                #self.my_marty.play_mp3("sounds/Connect.mp3")
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
        self.calibrationButton.show()
        self.isControlled = False
        
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
            self.control_button.hide()
            self.isControlled = True
        else:
            print("No marty object available")
            self.homeClicked()
            
    def calibrationClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.calibrationButton.show()
        
        self.my_marty = self.getMyMarty()
        if self.my_marty is not None:
            self.homeButton.show()
            self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            self.setFocus()
            self.calibrationButton.hide()
            self.isControlled = True
            
            self.redButton.show()
            self.greenButton.show() 
            self.blueButton.show()
            self.lightBlueButton.show()
            self.yellowButton.show()
            self.pinkButton.show()
            self.blackButton.show()
        else:
            print("No marty object available")
            self.homeClicked()

    def keyPressEvent(self, event):
        if self.isControlled:
            if self.my_marty is not None:
                #basic movement
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
                elif event.key() == Qt.Key.Key_A:
                    rotate(self.my_marty, -15)
                    print("rotating left")
                elif event.key() == Qt.Key.Key_E:
                    rotate(self.my_marty, 15)
                    print("rotating right")
                #emotes
                elif event.key() == Qt.Key.Key_1:
                    self.my_marty.celebrate()
                    self.my_marty.play_sound("whisle")
                    print("celebration in progress !")
                elif event.key() == Qt.Key.Key_2:
                    self.my_marty.dance()
                    self.my_marty.play_sound("whisle")
                    print("dancing in progress !")
                elif event.key() == Qt.Key.Key_3:
                    self.my_marty.circle_dance()
                    print("circle dancing in progress !")
                elif event.key() == Qt.Key.Key_4:
                    self.my_marty.circle_dance()
                    print("circle dancing in progress !")
                elif event.key() == Qt.Key.Key_5:
                    self.my_marty.kick('left', 180, 1000)
                    print("kicking left leg")
                elif event.key() == Qt.Key.Key_6:
                    self.my_marty.lean("forward", 100, 1000)
                    print("leaning forward")
                elif event.key() == Qt.Key.Key_7:
                    self.my_marty.arms(135, 0, 1000)
                    print("raising arms")
                elif event.key() == Qt.Key.Key_Escape:
                    self.my_marty.stop("pause")
                    print("stopping")
                elif event.key() == Qt.Key.Key_L:
                    print("l")
                    labyrintheColor(self.my_marty)
                    print("labyrinthe")
                else:
                    print("Key not recognized")
            else:
                print("No marty object available")
    
    
    def redClicked(self):
        Calibrage(self.my_marty,"red")
    
    def greenClicked(self):
        Calibrage(self.my_marty,"green")
        
    def blueClicked(self):
        Calibrage(self.my_marty,"blue")
        
    def lightBlueClicked(self):
        Calibrage(self.my_marty,"lightblue")
        
    def yellowClicked(self):
        Calibrage(self.my_marty,"yellow")
        
    def pinkClicked(self):
        Calibrage(self.my_marty,"pink")
        
    def blackClicked(self):
        Calibrage(self.my_marty,"black")
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MartyRobotController()
    controller.show()
    sys.exit(app.exec())