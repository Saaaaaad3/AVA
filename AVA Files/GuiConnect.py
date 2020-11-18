from PyQt5.QtWidgets import QLabel, QLineEdit,QPushButton,QStackedWidget,QMainWindow,QApplication, QInputDialog
from PyQt5.QtCore import Qt , QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import CommandInput as CInput 
import AssistantSpeak as ASpeak
import ModelIntegration
import Weather
import CommonFunctions as CF
import GoogleCalender as Gcalender
import UserEmail
import GoogleTranslate as Gtranslate
import os
import webbrowser
import Notes
import wolframalphafile

speak = ASpeak.speak

ui,_ = loadUiType('icons\\AVA.ui')

GLOBAL_STATE = 0
WAKE = 'hello'


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

        #Right Three Buttons 
        self.closebtn.clicked.connect(lambda: self.close())
        self.Minimize.clicked.connect(lambda: self.showMinimized())
        #self.MaxWindowbtn.clicked.connect(lambda: self.showMaximized())
        self.MaxWindowbtn.clicked.connect(lambda: self.maximize_restore())

    def ShowDiag(self):
        text, result = QInputDialog.getText(self, 'Enter Here', 'Command: ')
        return text

    def Handle_Text(self):
        self.lineEdit.returnPressed.connect(self.process)

    def setTB(self,text):
        OP = self.OutputTB.setText(text)
        self.lineEdit.clear()

    
    def process(self):
        sentence = self.lineEdit.text().lower()
        SERVICE = Gcalender.authenticate_google()
        botresponse = ModelIntegration.MLFunc(sentence)
        
        if botresponse != None:

            if "poweroff" in sentence or "exit" in sentence:
                self.close()

            elif "weather" in botresponse:
                self.setTB(speak("which City ?"))
                self.command = self.ShowDiag()
                try:
                    self.setTB(Weather.weatherreport((self.command)))
                except Exception as e :
                    self.setTB(speak("An Error Occured"))

            elif "event" in botresponse:
                date = Gcalender.get_date(sentence)
                if date:
                    self.setTB(speak(Gcalender.get_events(date,SERVICE)))
                else:
                    self.setTB(speak("I dont understand"))

            elif "mail" in botresponse:
                try:
                    self.setTB("Enter the Recipient")
                    to = self.ShowDiag()

                    self.setTB(speak("Enter the subject"))
                    subject = self.ShowDiag()

                    self.setTB(speak("What should I write?"))
                    content = self.ShowDiag()

                    UserEmail.SendSubEmail(to,subject,content)
                    self.setTB(speak("Email has been sent"))
                except Exception as e:
                    print(e)
                    self.setTB(speak("An Error has occured"))

            elif "news" in botresponse:
                self.setTB(speak(CF.shownews())) #Not Sorted out yet!! #######
            
            elif "screenshot" in botresponse:
                self.setTB(speak(CF.takescreenshot()))
            
            elif "translate" in botresponse:
                self.setTB(speak("Enter the language you want to translate from"))
                inputlang = self.ShowDiag()
                self.setTB(speak("Enter the text"))
                userinput = self.ShowDiag()
                self.setTB(speak("Enter the language you want to translate to"))
                lang = self.ShowDiag()

                self.setTB(speak(Gtranslate.translatesentence(inputlang,userinput,lang)))

            elif "shutdown" in botresponse:
                self.setTB("Do you wish to shutdown the system ?")
                command = self.ShowDiag()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /s /t 1")
                else:
                    pass

            elif "restart" in botresponse:
                self.setTB("Do you wish to restart the system ?")
                command = self.ShowDiag()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /r /t 1")
                else:
                    pass

            elif "maps" in botresponse: #Not Sorted out!!
                self.setTB(speak("Which place should i search for ?"))
                place = self.ShowDiag()
                webbrowser.open("https://www.google.com/maps/place/" + place)

            elif "reddit" in botresponse:
                try: 
                    self.setTB("Which subbreddit ?")
                    subreddit = self.ShowDiag()
                    subreddit = subreddit.replace(" ","")
                    webbrowser.open_new_tab('www.reddit.com/r/' + subreddit)
                except Exception as e:
                    print(e)
                    self.setTB(speak("Something Went wrong"))
                    
            elif "note" in botresponse:
                self.setTB("What should i write down ?")
                note_text = self.ShowDiag()
                Notes.instantnote(note_text)
                self.setTB(speak("I've made a note of that"))

            elif "console" in botresponse:
                self.setTB(speak("Opening your Playstore Console"))
                webbrowser.open_new_tab("https://play.google.com/console/u/0/developers/5469473923678169464/app-list")
            
            elif "insta" in botresponse:
                self.setTB("Initializing")
                CF.instagram()
            
            elif "wiki" in botresponse:
                self.setTB(speak("What do you want me to search on wikipedia ?"))
                wikisearch = self.ShowDiag()
                self.setTB(speak(CF.wiki(wikisearch)))

            elif "wolfram" in botresponse:
                self.setTB(speak("Ask me"))
                self.wolframquery = self.ShowDiag()
                self.setTB(speak(wolframalphafile.wolframfunc(self.wolframquery)))
            
            elif "read" in botresponse:
                self.setTB(EM.copydata())

            elif "copy" in botresponse:
                EM.copy()
                self.setTB("Copied")

            elif "paste" in botresponse:
                EM.paste()

            elif "time" in botresponse:
                self.setTB(speak(CF.timetoday()))

            elif "date" in botresponse:
                self.setTB(speak(CF.daytoday()))

            else:
                self.setTB(speak("I dont understand you. Please be more specific"))
        else:
            self.setTB(speak("Please try again"))

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
