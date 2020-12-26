import os
import pyttsx3
import webbrowser
import speech_recognition as sr
pyttsx3.speak("Hellow buddy! I am Ceraa, your mini assistant. Which app you want to use?")
pyttsx3.speak("Enter your choice")
while True:
    print("Anything else?", end=" ")

    #p=input()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("I am listening.")
        audio=r.listen(source)
        pyttsx3.speak("OK! I got it.")

    p=r.recognize_google(audio)

    if ("date" in p):
        pyttsx3.speak("here you go!")
        webbrowser.open("http://192.168.43.105/cgi-bin/f.py?c=date")
    elif ("calender" in p):
        pyttsx3.speak("Here you go!")
        webbrowser.open("http://192.168.43.105/cgi-bin/f.py?c=cal")
    elif((("don't" in p) or ("dont" in p)) and (("notepad" in p) or ("chrome" in p) or ("Notepad" in p) or ("Chrome" in p))):
        pyttsx3.speak("Ok! Kindly tell me your next choice")
    elif("chrome" in p or "internet" in p or "Chrome" in p or "Internet" in p):
        pyttsx3.speak("Here you go!")
        os.system("chrome")
    elif("notepad" in p or "text" in p or "editor" in p or "Notepad" in p or "Text" in p or "Editor" in p):
        pyttsx3.speak("Here you go!")
        os.system("notepad")
    elif("stop" in p or "exit" in p or "sleep" in p or "thank you" in p or "bye" in p or "sayonara" in p or "rest" in p):
        pyttsx3.speak("Thank you for using me. See you soon!")
        break
    else:
        pyttsx3.speak("Sorry! Still trying to make it better")
