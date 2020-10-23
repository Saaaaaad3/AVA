import re
import webbrowser
import AssistantSpeak as ASpeak
import pyautogui
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

speak = ASpeak.speak

"""
def openreddit(Vinput):
    try:
        #reg_ex = re.search('open reddit (.*)', Vinput)
        url = 'https://www.reddit.com/r/'
        
        if reg_ex:
            subreddit = reg_ex.group(1).replace(" ", "")
            url = url + 'r/' + subreddit
            webbrowser.open(url)
            print("Subreddit opened")

    except Exception as e:
        print(e)
        speak("Something Went wrong.")
"""

def takescreenshot():
    #Saves Screen shot with the system's current Date and time
    try:
        myscreenshot = pyautogui.screenshot()
        filename = (time.strftime("%d-%m-%Y--%H.%M.%S") + ".png")
        myscreenshot.save("C:\\Users\\dell\\Pictures\\Screenshots\\" + filename)
                    
    except Exception as e:
        speak("Something went wrong")
        print(e)

def shownews():
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "lxml-xml")
        news_list = soup_page.findAll("item")
        newscount = 0

        for news in news_list:
            if newscount < 5:
                speak(news.title.text)
                print(news.pubDate.text)
                print("-" * 50)
                newscount += 1

    except Exception as e:
        print(e)