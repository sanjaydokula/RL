from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton,QFileDialog
from PyQt6.QtGui import QIcon, QAction
from PyQt6 import QtGui
from PyQt6 import QtCore
import sys
from PyQt6.QtCore import QProcess,QFileInfo
from ModelLoad import Model
import os
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
        self.parameters ={'modelpath':"",'envname':""}
        self.home()

    def home(self):
        
        
        self.quit_btn = QAction("quit",self)
        self.quit_btn.setCheckable(True)
        self.quit_btn.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.snake = QAction("load snake env",self)
        self.snake.setCheckable(True)
        self.snake.triggered.connect(self.load_snake_model)

        self.run_btn = QPushButton("play",self)
        # self.run_btn.setCheckable(True)
        self.run_btn.clicked.connect(self.run)
        self.run_btn.move(200,100)

        self.compile_btn = QPushButton("compile agent",self)
        # self.run_btn.setCheckable(True)
        self.compile_btn.clicked.connect(self.compile)
        self.compile_btn.move(200,150)

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
        filepath,wot = QFileDialog.getOpenFileName(self,"open model","~","model files(*.zip)")
        
        # print(wot)
        # self.filename = QFileInfo(file).fileName()
        # print(type(self.filename[:-4]))
        # print(self.filename[:-4])

        path = os.path.normpath(filepath)
        path = path.split(os.path.sep)
        mod = f"{path[-3]}/{path[-2]}/{path[-1]}"
        self.filename = mod
        self.parameters['modelpath'] = self.filename
        print(mod)
        # self.model = Model(self.filename,self.envName)

    def select_environment(self):
        action = self.sender()
        self.envName = action.text()
        print("action: ", self.envName)
        self.parameters['envname'] = self.envName
        # self.model = Model(self.filename,self.envName)
    
    def compile(self):
        self.model = Model(self.parameters['modelpath'],self.parameters['envname'])


app = QApplication(sys.argv)
GUI = Window()
# GUI.cmd
sys.exit(app.exec())
