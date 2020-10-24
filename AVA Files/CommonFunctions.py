import re
import webbrowser
import AssistantSpeak as ASpeak
import pyautogui
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import CommandInput as CInput

speak = ASpeak.speak


chrome_path = "C:\Program Files (x86)\Google\Chrome\Application"

def takescreenshot():
    #Saves Screen shot with the system's current Date and time
    try:
        myscreenshot = pyautogui.screenshot()
        filename = (time.strftime("%d-%m-%Y--%H.%M.%S") + ".png")
        myscreenshot.save("C:\\Users\\dell\\Pictures\\Screenshots\\" + filename)
        speak("ScreenShot Saved")

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

def searchnet(command):
    try:
        webbrowser.open_new_tab(command)
    except Exception as e:
        print("Something Went wrong")
        print(e)

        
def instagram():
    
    try: 
        webbrowser.open("https://www.instagram.com")
    except Exception as e:
        print(e)
        print("Something went wrong")
