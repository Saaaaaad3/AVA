from PyQt5.QtWidgets import *

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys      

ui,_ = loadUiType('icons\\AVA.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.Homebtn_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.AVAbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.CmdListbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settingbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.aboutbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

    def OpenHomePage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def OpenAvaPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def OpenCommandListPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def OpenSettingsPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def OpenAboutPage(self):
        self.stackedWidget.setCurrentIndex(4)


























def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()