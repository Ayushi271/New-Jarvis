import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
from DataBase.ExtraPro.Alarm import RingerNow
from geopy.geocoders import Nominatim

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("googlesearch","")
    query = query.replace("who is","")
    query = query.replace("what do you mean by","")

    Query = str(query)
    pywhatkit.search(Query)

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Ma'am .")

def Alarm(query):

    TimeHere= open('C:\\Users\\HP\\OneDrive\\Desktop\\New Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\New Jarvis\\DataBase\\ExtraPro\\Alarm.py")
     



def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/United+College+of+Engineering+and+Research/@25.3423492,81.8959867,804m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3985497f856b1d35:0xf727c4fc418f7b"

    Speak("Checking....")

    web.open(op)

    
    loc = Nominatim(user_agent="GetLoc")
    
    
    getLoc = loc.geocode("Naini Prayagraj")
    
    print(getLoc.address)
    Speak(f"Ma'am , You Are Now In {getLoc.address} .")

