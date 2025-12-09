
import pyttsx3 as p
import speech_recognition as sr
import pyaudio
from seleniom_web import Infow
from yt  import *
from news import *
import randfacts
from jokes import *
import datetime
from datetime import datetime
from date_time import get_time, get_date


def speak(text):

    engine = p.init()
    engine.setProperty('rate', 190)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

today_date = datetime.now()


r = sr.Recognizer()


speak("Hello Mam, I am your voice assistant.")
speak("how are you..??")
with sr.Microphone() as source:
    r.energy_threshold = 300
    r.adjust_for_ambient_noise(source, 0.2)
    print(" Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    text = text.lower()
    print("You said:", text)

    if "what" in text and "about" in text and "you" in text:
        speak("I am having a good day mam. What can I do for you..?")
    elif "hello" in text:
        speak("Hello mam, nice to hear from you again!")
        speak("what can i do for you..?")
    elif "who are you" in text:
        speak("I am your voice assistant, created to help you, mam!")
        speak("what can i do for you..??")
    else:
        speak("I heard you say " + text )
        speak("glad to hear that..")
        speak("what can i do for you..??")

except sr.UnknownValueError:
    speak("Sorry mam, I didn’t catch that. Can you say it again..?")
except sr.RequestError:
    speak("Please check your internet connection, mam.")

with sr.Microphone() as source:
    r.energy_threshold = 300
    r.adjust_for_ambient_noise(source, 0.2)
    print('listening..')
    audio = r.listen(source)
    text2 = r.recognize_google(audio)


if "information" in text2:
    speak('you need information related to which topic..?')

    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, 0.2)
        print('listening..')
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching  {}  in wikipedia".format(infor))
    assist = Infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("you want me to play which video..??")
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, 0.2)
        print('listening..')
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak('playing {} on youtube'.format(vid))
    print('playing {} on youtube'.format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("sure mam i will read news for you")
    speak("sure mam i will read news for you")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2 or "facts" in text2:
    speak("sure mam...")
    x= randfacts.get_fact()
    print(x)
    speak(" Did you know that, " + x)

elif "joke" in text2 or "jokes" in text2:
    speak("sure mam, get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "time" in text2:
    speak(get_time())

elif "date" in text2:
    speak(get_date())

