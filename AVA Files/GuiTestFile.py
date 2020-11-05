from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import TestFile as TF      

ui,_ = loadUiType('icons\\AVA.ui')

GLOBAL_STATE = 0

class MainApp(QMainWindow, ui):

    GLOBAL_STATE = 0


    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)  #Removes Title bar
        self.setAttribute(Qt.WA_TranslucentBackground) #Removes the remaining border
        self.homegif()
        self.Avagif()
        self.Handle_Buttons()
        self.Handle_Text()

##### Title Bar Drag and Drop #####
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
#######


    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)


    def Avagif(self):
        self.movie = QMovie("icons\\LogoGif\\Blue Orb.gif")
        self.AVAGif_label.setMovie(self.movie)
        self.movie.start()


    def homegif(self):
        self.movie = QMovie("icons\\LogoGif.gif")
        self.TopLabel.setMovie(self.movie)
        self.movie.start()


    def Handle_Buttons(self):
        # Upper Buttons
        self.Homebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.AVAbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.CmdListbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settingbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.aboutbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        # Lower Buttons
        self.SpeechInputbtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.TypeInputbtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))

        self.closebtn.clicked.connect(lambda: self.close())
        self.Minimize.clicked.connect(lambda: self.showMinimized())
        #self.MaxWindowbtn.clicked.connect(lambda: self.showMaximized())
        self.MaxWindowbtn.clicked.connect(lambda: self.maximize_restore())


    def Handle_Text(self):
        self.lineEdit.returnPressed.connect(self.onPressed)



    def onPressed(self):
        self.OutputTB.setText(TF.ActualBot(self.lineEdit.text()))
        self.lineEdit.clear()















def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()