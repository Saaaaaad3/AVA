import wolframalpha 
import AssistantSpeak as ASpeak

speak = ASpeak.speak

app_id = '97662V-HGH7Y35KE4' 

client = wolframalpha.Client(app_id)


def wolframfunc(question):

    try:
        res = client.query(question) 
        answer = next(res.results).text 
        speak(answer)
    except Exception as e:
        speak("Something went wromg")
