import speech_recognition as sr

#Gets the audio input from the user, from the active microphone
def VoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""           #Empty 'said' variable initialized to later on append the input command

        try:
            said = r.recognize_google(audio)
            print(said)         #Prints the user's audio input for user's verification

        except Exception as e:
            print(e)
            
    return said.lower()         #lowers the input to avoid any errors due to capitalization and ease of recognization



    