#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

import sys

from application.connexion import *
from application.deplacement import *

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QProgressBar, QVBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QIcon, QKeyEvent
from application.connexion import connexion
from application.labyrinthe import getLabyrintheColor,executeLabyrinthe,correction
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
                border-image: url('src/img/background.jpg') 0 0 0 0 stretch stretch;
            }
        """)
        
    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def initUI(self):
        self.setWindowTitle("Marty Robot Controller")
        self.setGeometry(200, 100, 1260, 800)
        self.setWindowIcon(QIcon("src/img/robot_icon.ico"))
        
        self.my_marty = None
        self.my_marty2 = None
        self.currentRobot = None
        self.tableau = [] 
        self.battery1 = 0
        self.battery2 = 0

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

        #create battery bar for first robot
        self.batteryBar1 = QProgressBar()
        self.batteryBar1.setRange(0, 100)
        self.batteryBar1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.batteryBar1.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey; 
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #05B8CC;
                width: 10px;
            }
        """)
        self.batteryBar1.hide()
        
        #create battery bar for second robot
        self.batteryBar2 = QProgressBar()
        self.batteryBar2.setRange(0, 100)
        self.batteryBar2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.batteryBar2.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #05B8CC;
                width: 10px;
            }
        """)
        self.batteryBar2.hide()

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
        
        # Style the first robot button
        self.firstRobot = QPushButton("First Robot")
        self.firstRobot.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.firstRobot.clicked.connect(self.firstRobotClicked)
        self.firstRobot.hide()
        
        # Style the second robot button
        self.secondRobot = QPushButton("Second Robot")
        self.secondRobot.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.secondRobot.clicked.connect(self.secondRobotClicked)
        self.secondRobot.hide()
        
        # Sentence to display the choice of the robot
        self.sentence = QLabel("Choose the robot you want to control !")
        self.sentence.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sentence.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 60px;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
            }
        """)
        self.sentence.hide()
        
        # Style the Labyrinthe button
        self.labyrintheButton = QPushButton("Labyrinthe")
        self.labyrintheButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 200px;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        self.labyrintheButton.clicked.connect(self.labyrintheClicked)
        self.labyrintheButton.hide()
        
        # Style the main title
        self.mainTitle = QLabel("Marty Robot Controller")
        self.mainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainTitle.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 80px;
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
        
        # Style the WiFi button
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
        grid.addWidget(self.greenButton, 3, 1, 1, 1)
        grid.addWidget(self.blueButton, 1, 0, 1, 1)
        grid.addWidget(self.lightBlueButton, 1, 1, 1, 1)
        grid.addWidget(self.yellowButton, 2, 0, 1, 1)
        grid.addWidget(self.pinkButton, 2, 1, 1, 1)
        grid.addWidget(self.blackButton, 3, 0, 1, 1)
        
        grid.addWidget(self.firstRobot, 2, 0, 1, 1)
        grid.addWidget(self.secondRobot, 2, 1, 1, 1)
        grid.addWidget(self.sentence, 1, 0, 1, 2)
        grid.addWidget(self.labyrintheButton, 0, 0, 1, 1)
        
        grid.addWidget(self.batteryBar1, 3, 0, 1, 2)
        grid.addWidget(self.batteryBar2, 4, 0, 1, 2)

        self.setLayout(grid)

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def usbClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.loadingScreen.show()
        self.loadingBar.show()
        self.homeButton.show()
        (connecter, my_marty)=connexion(False)
        if(connecter):
            print("Le robot est connecté")
            #self.my_marty.play_mp3("sounds/Connect.mp3")
            self.my_marty = my_marty

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def wifiClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.ipAddress.show()
        self.homeButton.show()
        self.ipAddress.returnPressed.connect(self.onReturnPressed)
        
    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def onReturnPressed(self):
        
        
        if self.ipAddress.text() == "":
            (connecter,my_marty)=connexion(True)  
            if (connecter):
                if (self.my_marty is not None):
                    print("le deuxième robot est connecté")
                    self.my_marty2 = my_marty
                    #self.my_marty.play_mp3("src\sounds\Connect.mp3")
                    self.battery2 = self.my_marty2.get_battery_remaining()
                    self.batteryBar2.setValue(self.battery2)
                    
                if (self.my_marty is None):
                    print("le premier robot est connecté")
                    self.my_marty = my_marty
                    #self.my_marty.play_mp3("src\sounds\Connect.mp3")
                    self.battery1 = self.my_marty.get_battery_remaining()
                    self.batteryBar1.setValue(self.battery1)
        else:
            (connecter,my_marty)=connexion(True, self.ipAddress.text())
            if (connecter):
                if (self.my_marty is not None):
                    print("le deuxième robot est connecté")
                    self.my_marty2 = my_marty
                    #self.my_marty.play_mp3("src\sounds\Connect.mp3")
                    self.battery2 = self.my_marty2.get_battery_remaining()
                    self.batteryBar2.setValue(self.battery2)
                    self.batteryBar2.show()
                if (self.my_marty is None):
                    print("le premier robot est connecté")
                    self.my_marty = my_marty
                    #self.my_marty.play_mp3("src\sounds\Connect.mp3")
                    self.battery1 = self.my_marty.get_battery_remaining()
                    self.batteryBar1.setValue(self.battery1)
                    self.batteryBar1.show()

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def getMyMarty(self):
        return self.my_marty

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

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
        
        self.batteryBar1.setValue(self.battery1)
        self.batteryBar2.setValue(self.battery2)
        
        self.batteryBar1.show()
        self.batteryBar2.show()

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def firstRobotClicked(self):
        self.firstRobot.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;  /* Change the background color to red */
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
        self.secondRobot.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Back to normal */
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
        print("first robot selected")
        self.currentRobot = self.my_marty

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def secondRobotClicked(self):
        self.secondRobot.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;  /* Change the background color to red */
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
        self.firstRobot.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Back to normal */
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
        print("second robot selected")
        self.currentRobot = self.my_marty2

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def controlClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        
        if self.my_marty is not None or self.my_marty2 is not None:  
            self.control_button.hide()
            self.firstRobot.show()
            self.secondRobot.show()
            self.sentence.show()
            self.homeButton.show()
            self.labyrintheButton.show()

            self.batteryBar1.show()
            self.batteryBar2.show()

            self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            self.setFocus()
            self.control_button.hide()
            self.isControlled = True
        else:
            print("No marty object available")
            self.homeClicked()

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------
          
    def calibrationClicked(self):
        vbox = self.layout()
        for i in range(vbox.count()): 
            widget = vbox.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.calibrationButton.show()
        
        if self.my_marty is not None or self.my_marty2 is not None:
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

            self.batteryBar1.hide()
            self.batteryBar2.hide()
        else:
            print("No marty object available")
            self.homeClicked()

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def keyPressEvent(self, event):
        if self.isControlled:
            if self.currentRobot is not None:
                #basic movement
                if event.key() == Qt.Key.Key_Z:
                    movementDirection(self.currentRobot,"forward")
                    print("walking forward")
                elif event.key() == Qt.Key.Key_S:
                    movementDirection(self.currentRobot,"backwards")
                    print("walking backward")
                elif event.key() == Qt.Key.Key_Q:
                    movementDirection(self.currentRobot,"left")
                    print("turning left")
                elif event.key() == Qt.Key.Key_D:
                    movementDirection(self.currentRobot,"right")
                    print("turning right")
                elif event.key() == Qt.Key.Key_A:
                    rotate(self.currentRobot, -15)
                    print("rotating left")
                elif event.key() == Qt.Key.Key_E:
                    rotate(self.currentRobot, 15)
                    print("rotating right")
                #emotes
                elif event.key() == Qt.Key.Key_1:
                    self.currentRobot.celebrate()
                    self.currentRobot.play_sound("whisle")
                    print("celebration in progress !")
                elif event.key() == Qt.Key.Key_2:
                    self.currentRobot.dance()
                    self.currentRobot.play_sound("whisle")
                    print("dancing in progress !")
                elif event.key() == Qt.Key.Key_3:
                    self.currentRobot.circle_dance()
                    print("circle dancing in progress !")
                elif event.key() == Qt.Key.Key_4:
                    self.currentRobot.circle_dance()
                    print("circle dancing in progress !")
                elif event.key() == Qt.Key.Key_5:
                    self.currentRobot.kick('left', 180, 1000)
                    print("kicking left leg")
                elif event.key() == Qt.Key.Key_6:
                    self.currentRobot.lean("forward", 100, 1000)
                    print("leaning forward")
                elif event.key() == Qt.Key.Key_7:
                    self.currentRobot.arms(135, 0, 1000)
                    print("raising arms")
                elif event.key() == Qt.Key.Key_Escape:
                    self.currentRobot.stop("pause")
                    print("stopping")
                elif event.key() == Qt.Key.Key_L:
                    print("l")
                    if self.currentRobot == self.my_marty:
                        #self.tableau=getLabyrintheColor(self.currentRobot, self.my_marty2)
                        self.tableau=[["lightblue","blue", "green"],
                                      ["blue", "yellow", "green"],
                                      ["red", "pink", "pink"]]
                        executeLabyrinthe(self.currentRobot, self.tableau)
                        print("labyrinthe")
                    elif self.currentRobot == self.my_marty2:
                        self.tableau=getLabyrintheColor(self.currentRobot, self.my_marty)
                        executeLabyrinthe(self.currentRobot, self.tableau)
                        print("labyrinthe")
                else:
                    print("Key not recognized")
            else:
                print("Please select a robot to control")
    
    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def redClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"red",1)
        else:Calibrage(self.currentRobot,"red",2)

    # ----------------------------------------------------------
    # Méthodes : Couleurs clickées
    # Description :
    # ----------------------------------------------------------
      
    def greenClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"green",1)
        else:Calibrage(self.currentRobot,"green",2)
        
    def blueClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"blue",1)
        else:Calibrage(self.currentRobot,"blue",2)
        
    def lightBlueClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"lightblue",1)
        else:Calibrage(self.currentRobot,"lightblue",2)
        
    def yellowClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"yellow",1)
        else:Calibrage(self.currentRobot,"yellow",2)
        
    def pinkClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"pink",1)
        else:Calibrage(self.currentRobot,"pink",2)
        
    def blackClicked(self):
        if (self.my_marty==self.currentRobot):Calibrage(self.currentRobot,"black",1)
        else:Calibrage(self.currentRobot,"black",2)        

    # ----------------------------------------------------------
    # Méthode : 
    # Description :
    # ----------------------------------------------------------

    def labyrintheClicked(self):
        oldTableau = correction(self.tableau )   
        tableau=[]
        for i in range(len(oldTableau)):
            for j in range(len(oldTableau[i])):
                tableau.append(oldTableau[2-i][2-j])
        # Open a new window
        self.newWindow = QWidget()
        self.newWindow.setWindowTitle("New Window")
        self.newWindow.setGeometry(QRect(100, 100, 600, 600))
        
        # Créer un QVBoxLayout pour la nouvelle fenêtre
        layout = QGridLayout()
        
        for index, color in enumerate(tableau):
            label = QLabel()
            label.setStyleSheet(f"background-color: {color};")
            # Calculer la ligne et la colonne pour un layout 3x3
            row = index // 3
            column = index % 3
            layout.addWidget(label, row, column)
        
        
        self.newWindow.setLayout(layout)  # Définir le layout pour newWindow
        
        self.newWindow.show()
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MartyRobotController()
    controller.show()
    sys.exit(app.exec())