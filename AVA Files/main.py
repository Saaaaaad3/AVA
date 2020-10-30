#Pre-Defined Modules
import webbrowser
import os

#User defined Modules
import GoogleCalender as Gcalender
import WishUser
import AssistantSpeak as ASpeak 
import Notes
import UserEmail
import CommonFunctions as CF
import Weather 
import GoogleTranslate as Gtranslate
import CommandInput as CInput
import EditorMode as EM
import SpeechInput as SInput


speak = ASpeak.speak

if __name__ == '__main__':
    # Wake Word
    WAKE = 'ava'
    SERVICE = Gcalender.authenticate_google()
    WishUser.wishuser()

    while True:
        print('Listening')
        # Change Vinput = VoiceCommand() to input voice commands
        Vinput = SInput.VoiceCommand()
        print(Vinput)

        if Vinput.count(WAKE) > 0:
            speak("I am Ready")
            Vinput = SInput.VoiceCommand()

            #Shows how many and which events you have on a specific date(input)
            if "what do i have on" in Vinput or "do i have plans on" in Vinput or "am i busy on" in Vinput or "What events" in Vinput:
                date = Gcalender.get_date(Vinput)
                if date:
                    Gcalender.get_events(date,SERVICE)
                else:
                    speak('I dont understand')                    
            
            # Makes a note and saves in txt format
            ################### Bug Solving ####################
            elif "make a note" in Vinput or "write this down" in Vinput or "remember this" in Vinput:
                speak("What would you like me to remember ?")
                note_text = CInput.get_command()
                Notes.instantnote(note_text)
                speak("I've made a not of that!")

            elif "write a mail" in Vinput or "send a mail" in Vinput or "send mail" in Vinput or "write mail" in Vinput:
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
                    speak("An Error has occured")

            #Searches for the keyword passed after 'Search
            elif 'search' in Vinput:
                #Vinput = Vinput.replace("search","")
                command = CInput.get_command()
                webbrowser.open(command)

            # Searches map for the input place
            # Currently supports Countries, States and Cities
            elif 'search in maps' in Vinput:
                Vinput = Vinput.replace("search in maps", "")
                webbrowser.open("https://www.google.com/maps/place/" + Vinput)

            # Opens a subreddit entered after the word 'reddit'
            elif "open reddit" in Vinput:
                try: 
                    Vinput = input("Which subreddit ?")
                    Vinput = Vinput.replace(" ","")
                    webbrowser.open_new_tab('www.reddit.com/r/' + Vinput)
                    speak("Opening reddit")
                except Exception as e:
                    speak("Something Went wrong")

                #CF.openreddit('www.reddit.com/r/' + Vinput)

            elif "take screenshot" in Vinput or "take screen shot" in Vinput or "screenshot" in Vinput or "screen shot" in Vinput or "screenshot this" in Vinput:
                CF.takescreenshot()
                speak('Screenshot Saved')

            elif "news for today" in Vinput or "todays news" in Vinput or "news today" in Vinput or "today's news"in Vinput:
                CF.shownews()

            elif "weather report" in Vinput:
                speak("Which City's weather report should i look for ?: ")
                command = CInput.get_command()
                command = command.lower()
                Weather.weatherreport(command)

            elif "translate" in Vinput:
                Gtranslate.translatesentence()

            elif "power off" in Vinput or "power down" in Vinput or 'powerdown' in Vinput or 'poweroff' in Vinput:
                exit()

            elif "shutdown system" in Vinput or "shutdown machine" in Vinput or "shutdown the machine" in Vinput:
                speak("Do you wish to shutdown the system ?")
                command = CInput.get_command()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /s /t 1")
                else:
                    pass

            elif "restart system" in Vinput or "restart machine" in Vinput or "restart the machine" in Vinput or "Restart the system" in Vinput:
                speak("Do you wish to restart the system ?")
                command = CInput.get_command()
                if(command == 'yes' or command =='yep' or command == 'sure'):
                    os.system("shutdown /r /t 1")
                else:
                    pass

            elif "read the selected" in Vinput or "read selected" in Vinput or "read selection" in Vinput:
                EM.copydata()
                
            elif "copy" in Vinput:
                EM.copy()
                speak("Copied")
            
            elif("paste") in Vinput:
                EM.paste()
            
            elif "talk to me in" in Vinput:
                pass
