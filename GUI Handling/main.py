# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Time Using Py GUI")
        self.setGeometry(500, 250, 800, 600)
        self.setWindowIcon(QIcon("PFP.jpg"))

        # Full window background
        self.setStyleSheet("background-color: #111;")

        label = QLabel("Namaste Bhailog", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(300, 200, 200, 50)

        # White text
        label.setStyleSheet("color: #fff;")
        label.setAlignment(Qt.AlignTop)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()