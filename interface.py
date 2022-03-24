# from imp import load_module
# from json import load
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton,QFileDialog
from PyQt6.QtGui import QIcon, QAction
from PyQt6 import QtGui
from PyQt6 import QtCore
import sys
from PyQt6.QtCore import QProcess,QFileInfo
from ModelLoad import Model
# from qlearning import load

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Reinforcement Learning")
        self.setWindowIcon(QIcon('forza_ferrari.png'))
        self.model = None
        self.filename = None
        self.envName = None
        self.home()

    def home(self):
        
        
        self.quit_btn = QAction("quit",self)
        self.quit_btn.setCheckable(True)
        self.quit_btn.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.snake = QAction("load snake env",self)
        self.snake.setCheckable(True)
        self.snake.triggered.connect(self.load_snake_model)
        # self.load_btn.move(100,20)

        # self.mountain = QAction("load mountain env",self)
        # self.mountain.setCheckable(True)
        # self.mountain.triggered.connect(self.load_model)

        self.run_btn = QPushButton("play",self)
        self.run_btn.setCheckable(True)
        self.run_btn.clicked.connect(self.run)
        self.run_btn.move(200,100)

        self.select_model = QAction("Select model",self)
        self.select_model.triggered.connect(self.load_model)
        self.Snake_env = QAction("Snake Environment",self)
        self.Snake_env.triggered.connect(self.select_environment)
        self.Mount_env = QAction("MountainCar Environment",self)
        self.Mount_env.triggered.connect(self.select_environment)
        self.statusBar()

        mainMenu = self.menuBar()


        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(self.quit_btn)


        envMenu = mainMenu.addMenu('&Env')
        envMenu.addAction(self.Snake_env)
        envMenu.addAction(self.Mount_env)


        modelMenu = mainMenu.addMenu('&Model')
        modelMenu.addAction(self.snake)
        modelMenu.addAction(self.select_model)


        self.show()

        
    def load_snake_model(self):
        self.model = Model()
    # def mountain(self):
    #     load()
    def run(self):
        self.model.run()

    def load_model(self):
        file,wot = QFileDialog.getOpenFileName(self,"open model","~","model files(*.zip)")
        print(wot)
        self.filename = QFileInfo(file).fileName()
        print(type(self.filename[:-4]))
        print(self.filename[:-4])
        self.model = Model(self.filename,self.envName)

    def select_environment(self):
        action = self.sender()
        self.envName = action.text()
        print("action: ", self.envName)
        self.model = Model(self.filename,self.envName)



app = QApplication(sys.argv)
GUI = Window()
# GUI.cmd
sys.exit(app.exec())
