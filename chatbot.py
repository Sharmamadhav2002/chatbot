import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18 :
        speak("good afternoon!")
    else:
        speak("good evevning!")
    speak(" hello i am a jarvis what can i do ")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        #logic for executing the task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            print(results.encode("utf-8"))
            speak(results) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music ' in query:
            music="C:\\Users\\madhavsharma\\Downloads\\music_dir"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))
        elif 'the time'in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")
        elif 'open code' in query:
            os.startfile("C:\\Users\\madhavsharma\\Desktop\\test.")
            
            
        