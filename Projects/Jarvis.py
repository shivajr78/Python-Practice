import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia



# Voice Function
engine = pyttsx3.init('sapi5')  #sapi5 used for taking voice
voices = engine.getProperty('voices')
#Print(voices[0].id) #print for name of voice
engine.setProperty('voices',voices[1].id)


# Speak Function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,Nikky")
    elif hour >=12 and hour <18:
        speak("Good Afternoon,Shiva")
    else:
        speak("Good Night,Shiva")

    speak("Its Sushma. Please tell me How may I help you")

#Take command Function :It takes microphone input from the user and return string output

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
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
        query = takeCommand().lower()

#logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            speak(results)