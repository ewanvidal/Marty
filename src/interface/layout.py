import sys

from application.connexion import *
from application.deplacement import *

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QPushButton

(connecter,my_marty)=connexion(True)

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
        print(my_marty.get_ground_sensor_reading('LeftColorSensor'))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()