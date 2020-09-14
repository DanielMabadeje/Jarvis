import pyttsx3 
import datetime
import speech_recognition as sr
engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")
    
    speak("Jarvis at your service, How may i HELP YOU")
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query  = r.recognize_google(audio language='en-in')
        print(query)
        
        
    except exception as e:
        print(e)
        
    return query

take()