import sys
from PySide6.QtWidgets import *

# Just a filler class and file for now with a basic window, will be changed a lot once other needed classes are in place - don't work on it right now

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RPG Cutscene Maker")

        layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()