import Weather
import GoogleTranslate as Gtranslate
import AssistantSpeak as ASpeak
import torch
import json
from ChatBot.model import NeuralNet
from ChatBot.nltk_utils import bag_of_words, tokenize
import random
import CommandInput as CInput
import GoogleCalender as Gcalender
import webbrowser
import CommonFunctions as CF
import GoogleTranslate as Gtranslate
import ModelIntegration as MIntegration
import UserEmail
import Notes

speak = ASpeak.speak
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
botresponse = ""
if __name__ == '__main__':
    WAKE = 'hello'
    SERVICE = Gcalender.authenticate_google()

    while True:
        print("Listening")
        sentence = CInput.get_command()

        if sentence.count(WAKE) > 0:
            speak("Im Ready")
            sentence = CInput.get_command()

            if "poweroff" in sentence or "power of" in sentence or "powerdown" in sentence or "power off" in sentence or "power down" in sentence:
                break
            
            botresponse = MIntegration.MLFunc(sentence)

            if "weather" in botresponse:
                speak("Which City's weather report should I look for ?")
                command = input()
                command = command.lower()
                Weather.weatherreport(command)
            
            elif "event" in botresponse:
                date = Gcalender.get_date(sentence)
                if date:
                    Gcalender.get_events(date,SERVICE)
                else:
                    speak("I dont understand")

            elif "send mail" in botresponse:
                try:
                    speak("Enter the Recipient")
                    to = str(input())

                    speak("Enter the subject")
                    subject = input()

                    speak("What should I write?")
                    content = input()

                    UserEmail.SendSubEmail(to,subject,content)
                    speak("Email has been sent")
                
                except Exception as e:
                    print(e)
                    speak("An Error has occured")

            #########BUG########
            elif "net search" in botresponse:
                speak("What should I search for ?")
                command = input()
                CF.searchnet(command)

            elif "news" in botresponse:
                CF.shownews()
            
            elif "take screenshot" in botresponse:
                CF.takescreenshot()
            
            elif "translate" in botresponse:
                Gtranslate.translatesentence()

            elif "shutdownsystem" in botresponse:
                speak("Do you wish to shutdown the system ?")
                command = CInput.get_command()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /s /t 1")
                else:
                    pass

            elif "restartsystem" in botresponse:
                speak("Do you wish to restart the system ?")
                command = CInput.get_command()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /r /t 1")
                else:
                    pass
            
            elif "makenote" in botresponse:
                speak("What would you like me to remember ?")
                note_text = CInput.get_command()
                Notes.instantnote(note_text)
                speak("I've made a not of that!")

            elif "search maps" in botresponse:
                speak("Which place should i search for ?")
                place = input()
                webbrowser.open("https://www.google.com/maps/place/" + place)

            elif "show reddit" in botresponse:
                try: 
                    subreddit = input("Which subreddit ?")
                    subreddit = subreddit.replace(" ","")
                    webbrowser.open_new_tab('www.reddit.com/r/' + subreddit)
                    speak("Opening reddit")
                except Exception as e:
                    speak("Something Went wrong")
                    
            elif "make note" in botresponse:
                speak("What should i write down ?")
                note_text = CInput.get_command()
                Notes.instantnote(note_text)
                speak("I've made a note of that")     

            elif "googleplay console" in botresponse:
                webbrowser.open_new_tab("https://play.google.com/console/u/0/developers/5469473923678169464/app-list")

            elif "instagram login":
                speak("Opening Instagram")
                CF.instagram()

            else:
                print("I can't do that yet..")
                            