import sys

from application.connexion import *
from application.deplacement import *

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QPushButton
from application.deplacement import rotate

(connecter,my_marty)=connexion(True)
obstSensorL = my_marty.get_obstacle_sensor_reading('left')
obstSensorR = my_marty.get_obstacle_sensor_reading('right')
print("obstSensorL: ",obstSensorL,"  |  obstSensorR:",obstSensorR)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        button = QPushButton("Couleur")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
        #obstacleL = my_marty.foot_obstacle_sensed('left')
        #obstacleR = my_marty.foot_obstacle_sensed('right')
        #obstSensorL = my_marty.get_obstacle_sensor_reading('left')
        #obstSensorR = my_marty.get_obstacle_sensor_reading('right')
        #print("ObstacleL: ",obstacleL,"  |  ObstacleR:",obstacleR,"  |  ","obstSensorL: ",obstSensorL,"  |  obstSensorR:",obstSensorR)
        print(my_marty.get_ground_sensor_reading('LeftColorSensor'))
        print("Red : " + str(my_marty.get_color_sensor_value_by_channel("left", "red")))
        print("Green : " + str(my_marty.get_color_sensor_value_by_channel("left", "green")))
        print("Blue : " + str(my_marty.get_color_sensor_value_by_channel("left", "blue")))
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()