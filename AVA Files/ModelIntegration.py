import torch
import json
from ChatBot.model import NeuralNet
from ChatBot.nltk_utils import bag_of_words, tokenize
import random
import AssistantSpeak as ASpeak

speak = ASpeak.speak

botresponse = ""
def MLFunc(sentence):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('json\\intents.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE)
    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]
    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)   
    _,predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                botresponse = random.choice(intent['responses'])
                return botresponse
                break
    else:
        speak("Either I cant listen you properly or that is out of my current knowledge")