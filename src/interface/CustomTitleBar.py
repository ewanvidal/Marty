from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super(CustomTitleBar, self).__init__(parent)
        self.setAutoFillBackground(True)

        # Layout de la barre de titre
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Label pour le titre
        self.title = QLabel("Mon Application")

        # Bouton de fermeture
        self.closeButton = QPushButton("X")
        self.closeButton.clicked.connect(self.on_close_clicked)

        # Ajout des widgets au layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.closeButton)

    def on_close_clicked(self):
        # Ferme la fenêtre parente
        self.window().close()