import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            talk("how can I help?")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dorian' in command:
                command = command.replace("dorian"," ")
                print(command)
    except:
        pass
    return command


def run_dorian():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        talk("playing..." + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')  # saati '%I : %M &p' yazarsak pm tipinde verir
        print(time)
        talk("Current time is : "+time)
    elif 'who the heck is' in command:
        person= command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('I have a headache')
    elif 'are you single' in command:
        talk("I'm in a relationship with wifi")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("I didn't understand you, please repeat")

run_dorian()


while True:      #durdurulmadığı muddetce calisir.
    run_dorian()


