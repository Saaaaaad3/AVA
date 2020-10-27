import wikipedia
import re
import webbrowser
import AssistantSpeak as ASpeak
import pyautogui
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import CommandInput as CInput
from datetime import datetime
from datetime import date


timestamp = 1528797322
now = datetime.now()
day_time = datetime.fromtimestamp(timestamp)


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

def wiki(command):
    try:
        result = wikipedia.summary(command, sentences = 5) 
        speak(result)
    except wiki.DisambiguationError as e:
        if e :
            speak("Please be more specific")
        else:
            speak("Something Went wrong")
    
def timetoday():
    time = now.strftime("%I:%M %p")
    speak("The time is " + time)

def daytoday():
    #day = day_time.strftime("%d %B")
    day = date.today().strftime("%d %B")
    dayofweek = now.weekday()
    if dayofweek == 0:
        dayofweek = ", Monday "
        
    elif dayofweek == 1:
        dayofweek = ", Tuesday "
        
    elif dayofweek == 2:
        dayofweek = ", Wednesday "
        
    elif dayofweek == 3:
        dayofweek = ", Thursday "
        
    elif dayofweek == 4:
        dayofweek = ", Friday "
        
    elif dayofweek == 5:
        dayofweek = ", Saturday "
        
    elif dayofweek == 6:
        dayofweek = ", Sunday "
    
    speak(day + dayofweek)
        
