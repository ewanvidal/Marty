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
from application.sensors import getColorReadingRGB

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QPushButton
from application.deplacement import rotate

(connecter,my_marty)=connexion(True)
obstSensorL = my_marty.get_obstacle_sensor_reading('left')
obstSensorR = my_marty.get_obstacle_sensor_reading('right')
print("obstSensorL: ",obstSensorL,"  |  obstSensorR:",obstSensorR)

# ----------------------------------------------------------
# Classe : MainWindow 
# Description : Classe pour tester les couleurs RGB et au début du projet
# ----------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        button = QPushButton("Couleur")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    # ----------------------------------------------------------
    # Fonction : Le bouton a  été clické
    # Description : Bouton qui permet de récupérer nos valeurs après le click
    # ----------------------------------------------------------

    def the_button_was_clicked(self):
        print("Clicked!")
        #obstacleL = my_marty.foot_obstacle_sensed('left')
        #obstacleR = my_marty.foot_obstacle_sensed('right')
        #obstSensorL = my_marty.get_obstacle_sensor_reading('left')
        #obstSensorR = my_marty.get_obstacle_sensor_reading('right')
        #print("ObstacleL: ",obstacleL,"  |  ObstacleR:",obstacleR,"  |  ","obstSensorL: ",obstSensorL,"  |  obstSensorR:",obstSensorR)
        print(getColorReadingRGB(my_marty))
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()