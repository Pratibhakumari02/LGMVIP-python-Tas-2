import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the recognizer and the engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture the voice command from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            return None
        return command.lower()

def process_command(command):
    """Process the voice command and respond accordingly."""
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif 'wikipedia' in command:
        speak("What should I search on Wikipedia?")
        search_query = listen()
        if search_query:
            results = wikipedia.summary(search_query, sentences=2)
            speak(f"According to Wikipedia, {results}")

    elif 'open' in command:
        if 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        else:
            speak("Sorry, I can only open YouTube and Google right now.")

    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I don't know that command.")

def main():
    speak("How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()