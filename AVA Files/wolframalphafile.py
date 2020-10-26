import wolframalpha 
import AssistantSpeak as ASpeak

app_id = '97662V-HGH7Y35KE4' 

client = wolframalpha.Client(app_id)


def wolframfunc(question):

    question = input('Question: ')

    res = client.query(question) 
    answer = next(res.results).text 
    return answer
