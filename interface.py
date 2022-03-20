# from imp import load_module
# from json import load
from json import load
from operator import mod
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon, QAction
from PyQt6 import QtGui
from PyQt6 import QtCore
import sys
from PyQt6.QtCore import QProcess
from ModelLoad import Model
from qlearning import load

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Reinforcement Learning")
        self.setWindowIcon(QIcon('forza_ferrari.png'))
        self.model = None
        self.home()

    def home(self):
        
        
        self.quit_btn = QAction("quit",self)
        self.quit_btn.setCheckable(True)
        self.quit_btn.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.snake = QAction("load snake env",self)
        self.snake.setCheckable(True)
        self.snake.triggered.connect(self.load_model)
        # self.load_btn.move(100,20)

        self.mountain = QAction("load mountain env",self)
        self.mountain.setCheckable(True)
        self.mountain.triggered.connect(self.load_model)

        self.run_btn = QPushButton("play",self)
        self.run_btn.setCheckable(True)
        self.run_btn.clicked.connect(self.run)
        self.run_btn.move(200,100)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(self.quit_btn)
        modelMenu = mainMenu.addMenu('&Env')
        modelMenu.addAction(self.snake)
        # modelMenu.addAction(self.mountain)
        # modelMenu.addAction(self.run_btn)

        self.show()
    def load_model(self):
        self.model = Model()
    # def mountain(self):
    #     load()
    def run(self):
        self.model.run()

app = QApplication(sys.argv)
GUI = Window()
# GUI.cmd
sys.exit(app.exec())
