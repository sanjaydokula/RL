from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon, QAction
from PyQt6 import QtGui
from PyQt6 import QtCore
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setGeometry(2000,50,500,300)
        self.setWindowTitle("Reinforcement Learning")
        self.setWindowIcon(QIcon('forza_ferrari.png'))
        self.home()

    def home(self):
        quit_btn = QPushButton("quit",self)
        quit_btn.setCheckable(True)
        
        quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec())
