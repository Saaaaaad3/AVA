import datetime
import AssistantSpeak as ASpeak


USER = 'Saad'

#Wish the user depending on the time of the day
def wishuser():
    dayTime = datetime.datetime.now().hour

    if dayTime >= 0 and dayTime <12:
        ASpeak.speak("Hi " + USER + ", Good Morning!")
    elif dayTime >= 12 and dayTime < 18:
        ASpeak.speak("Hi " + USER + ", Good Afternoon")
    else:
        ASpeak.speak("Hi " + USER + ", Good Evening")