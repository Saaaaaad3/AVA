import pyttsx3
import GoogleCalender as GC

# Function for assistant's speaking.
def speak(text):
    engine = pyttsx3.init() # initializes the pyttsx3 module
    engine.say(text)
    print(text)
    engine.runAndWait() #For speaking and waiting before picking up user's voice command
