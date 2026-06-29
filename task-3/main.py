from speech import speak, listen
from automation import *
from weather import get_weather
from ai_engine import ask_ai

speak("Hello Ajay. I am ready.")

while True:

    command = listen()

    if "youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    elif "google" in command:
        speak("Opening Google")
        open_google()

    elif "github" in command:
        speak("Opening GitHub")
        open_github()

    elif "weather" in command:
        weather = get_weather("hyderabad")
        speak(weather)

    elif "stop" in command:
        speak("Goodbye")
        break

    else:
        answer = ask_ai(command)
        speak(answer)