import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from openai import OpenAI
from api_keys import newsapi, openai_api_key  # Import API keys from api_keys
from ai_process import aiProcess  # Import the aiProcess function from ai_process.py
from musicLibrary import music  # Make sure musicLibrary.py exists in the same folder
from speech import speak

client = OpenAI(api_key=openai_api_key)

def processCommand(command):
    command = command.lower().strip()
    print(f"Processing command: {command}")
    print(f"DEBUG → Checking conditions for: '{command}'")  # Yeh extra add karo

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open twitter" in command or "open x" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif command.startswith("play"):
        try:
            song = command.split(" ", 1)[1]  # Get everything after "play"
            if song in music:
                speak(f"Playing {song}")
                link = music[song]
                webbrowser.open(link)
            else:
                speak(f"Sorry, I don't have the song {song} in my library.")
        except IndexError:
            speak("Please say the song name after play.")

    elif "news" in command:
        speak("Fetching the latest news for you")
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if articles:
                    for article in articles[:5]:  # Only top 5 news
                        speak(article['title'])
                else:
                    speak("No news articles found.")
            else:
                speak("Sorry, I could not fetch the news right now.")
        except Exception as e:
            speak("There was a problem fetching the news.")

    else:
        # Let OpenAI handle unknown commands
        speak("Let me think...")
        output = aiProcess(command)
        speak(output)
