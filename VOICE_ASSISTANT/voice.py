import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyautogui
import pyjokes
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[1].id) #this print which audio you select
engine.setProperty('voice', voices[1].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic=pyautogui.screenshot()
    pic.save('c:/User')
def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >12 and hour <17:
        speak("good afternoon")    
    else:
        speak("good evening")
    speak("Hey i am zira, how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query


def joke():
    speak(pyjokes.get_jokes(language='en',category='all'))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()    

if __name__ == "__main__":
    wishme()
    while True:
    # if 3:
        # if 1:
        query = takeCommand().lower() 

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("what you want to listen")
            search= takeCommand().lower()
            speak('find some related vidoes ')
            webbrowser.open('https://www.youtube.com/results?search_query='+search) 
        elif 'open chrome' in  query:
            webbrowser.open("chrome.com")   

        elif 'open github' in query:
            search = takeCommand().lower()
            webbrowser.open('https://github.com/explore'+search)       
        elif 'open google' in query:
            speak("what i am search for you")
            search=takeCommand().lower()
            speak('these are the related results')
            webbrowser.open('https://www.google.co.in/search?q='+search)
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open stakoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        elif 'open college website' in query:
            webbrowser.open("https://www.iemcrp.com/")    

        elif 'joke' in query:
            joke()    
            print(joke)
        elif 'screenshot' in query:
            screenshot()    


        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            d=random.choice(songs)
            os.startfile(os.path.join(music_dir, d))   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"aman, the time is{strTime}")  
            print(strTime)       
        elif 'open vscode' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)      

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend aman bhai. I am not able to send this email")   
        elif 'shutdown' in query:
            print("shutting down...")
            speak("shutting down")
            quit()  
        elif 'exit' in query:
            print("exit the window...")
            speak("now i am exit")
            quit()           