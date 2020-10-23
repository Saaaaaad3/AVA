from googletrans import Translator
import AssistantSpeak as ASpeak

speak = ASpeak.speak

translator = Translator()

def translatesentence():

    speak("From which language do you want to translate: ")
    inputlang = input()

    speak("Enter the text: ")
    userinput = input()

    speak("Which language you want it to be translated to : ")
    lang = input().lower()

    try:

        result = translator.translate(userinput, src=inputlang, dest=lang)

        speak("\nTranslated Text: " + result.text + "\nPronunciation: " + result.pronunciation +
                "\nTranslated from: " + result.src + "\nTranslated to: " + result.dest)

    except Exception as e:
        print("Something Went wrong")
        print(e)
