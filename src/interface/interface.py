import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from CustomTitleBar import CustomTitleBar

class MartyRobotController(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Marty Robot Controller")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout()
        
        # Add custom title bar
        self.titleBar = CustomTitleBar(self)
        self.layout.addWidget(self.titleBar)
        

        # Style the USB button
        usbButton = QPushButton("USB")
        usbButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        usbButton.clicked.connect(self.usbClicked)
        self.layout.addWidget(usbButton)

        # Style the WiFi button
        wifiButton = QPushButton("WiFi")
        wifiButton.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1976d2;
            }
            QPushButton:pressed {
                background-color: #1565c0;
            }
        """)
        wifiButton.clicked.connect(self.wifiClicked)
        self.layout.addWidget(wifiButton)

        self.ipInput = QLineEdit()
        self.ipInput.setPlaceholderText("Enter IP address")
        self.ipInput.hide()
        self.layout.addWidget(self.ipInput)

        self.setLayout(self.layout)

    def usbClicked(self):
        print("USB button clicked")

    def wifiClicked(self):
        for i in range(self.layout.count()): 
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.hide()
        self.ipInput.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MartyRobotController()
    controller.show()
    sys.exit(app.exec())