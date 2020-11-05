import Weather
import GoogleTranslate as Gtranslate
import AssistantSpeak as ASpeak
import torch
import json
from ChatBot.model import NeuralNet
from ChatBot.nltk_utils import bag_of_words, tokenize
import random
import SpeechInput as SInput
import CommandInput as CInput
import GoogleCalender as Gcalender
import webbrowser
import CommonFunctions as CF
import GoogleTranslate as Gtranslate
import ModelIntegration as MIntegration
import UserEmail
import Notes
import wolframalphafile as WRFile
import EditorMode as EM
import os

speak = ASpeak.speak
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
botresponse = ""
def ActualBot(sentence):
    if __name__ == '__main__':
        WAKE = 'hello'
        SERVICE = Gcalender.authenticate_google()

        while True:
            print("Listening")
            sentence = CInput.get_command()
            #sentence = SInput.VoiceCommand()

            if sentence.count(WAKE) > 0:
                speak("Im ready")
                sentence = CInput.get_command()
                #sentence = SInput.VoiceCommand()
                if "poweroff" in sentence or "power of" in sentence or "powerdown" in sentence or "power off" in sentence or "power down" in sentence or "powerof" in sentence:
                    break
                
                botresponse = MIntegration.MLFunc(sentence)
                
                if botresponse == None:
                    pass

                elif "weather" in botresponse:
                    speak("Which City's weather report should I look for ?")
                    command = input()
                    #command = SInpuy.VoiceCommand()
                    command = command.lower()
                    Weather.weatherreport(command)
                
                elif "event" in botresponse:
                    date = Gcalender.get_date(sentence)
                    if date:
                        Gcalender.get_events(date,SERVICE)
                    else:
                        speak("I dont understand")

                elif "mail" in botresponse:
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
                elif "search" in botresponse:
                    speak("What should I search for ?")
                    command = input()
                    #command = SInput.VoiceCommand()
                    CF.searchnet(command)

                elif "news" in botresponse:
                    CF.shownews()
                
                elif "screenshot" in botresponse:
                    CF.takescreenshot()
                
                elif "translate" in botresponse:
                    Gtranslate.translatesentence()

                elif "shutdown" in botresponse:
                    speak("Do you wish to shutdown the system ?")
                    command = CInput.get_command()
                    #command = SInput.VoiceCommand()
                    if(command == 'yes' or command =='yep' or command == 'sure'):
                        os.system("shutdown /s /t 1")
                    else:
                        pass

                elif "restart" in botresponse:
                    speak("Do you wish to restart the system ?")
                    command = CInput.get_command()
                    #command = SInput.VoiceCommand()
                    if(command == 'yes' or command =='yep' or command == 'sure'):
                        os.system("shutdown /r /t 1")
                    else:
                        pass

                elif "maps" in botresponse:
                    speak("Which place should i search for ?")
                    place = input()
                    #place = SInput.VoiceCommand()
                    webbrowser.open("https://www.google.com/maps/place/" + place)

                elif "reddit" in botresponse:
                    try: 
                        subreddit = input("Which subreddit ?")
                        #subreddit = SInput.VoiceCommand()
                        subreddit = subreddit.replace(" ","")
                        webbrowser.open_new_tab('www.reddit.com/r/' + subreddit)
                        speak("Opening reddit")
                    except Exception as e:
                        speak("Something Went wrong")
                        
                elif "note" in botresponse:
                    speak("What should i write down ?")
                    note_text = CInput.get_command()
                    #note_text = SInput.VoiceCommand()
                    Notes.instantnote(note_text)
                    speak("I've made a note of that")     

                elif "console" in botresponse:
                    webbrowser.open_new_tab("https://play.google.com/console/u/0/developers/5469473923678169464/app-list")
                
                elif "insta" in botresponse:
                    speak("Initializing")
                    CF.instagram()
                
                elif "standby" in botresponse:
                    break
                
                elif "wiki" in botresponse:
                    speak("What do you want me to search on wikipedia ?")
                    wikisearch = CInput.get_command()
                    CF.wiki(wikisearch)

                elif "wolfram" in botresponse:
                    speak("Ask me")
                    wolframquery = CInput.get_command()
                    WRFile.wolframfunc(wolframquery)
                
                elif "read" in botresponse:
                    EM.copydata()

                elif "copy" in botresponse:
                    EM.copy()

                elif "paste" in botresponse:
                    EM.paste()

                elif "time" in botresponse:
                    CF.timetoday()

                elif "date" in botresponse:
                    CF.daytoday()

                else:
                    print("I dont understand you. Please be more specific")
                                
    return