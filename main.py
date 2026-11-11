# Modules import : 
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import sys

# CodePieces imports :
from ai_process import aiProcess  # Import the aiProcess function from ai_process.py
from api_keys import newsapi, openai_api_key  # Import API keys from api_keys.py
from utility_shack import processCommand  # Import the processCommand function from process_commands.py
from speech import speak
from speech import sr
print(sys.executable)

# ====================== MAIN PROGRAM ======================
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    print("Jarvis is ready!")

    mic_index = 1   # Realtek Microphone (change if needed)

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone(device_index=mic_index) as source:
                print("\nListening for wake word 'Jarvis'...")
                r.adjust_for_ambient_noise(source, duration=0.6)
                audio = r.listen(source, timeout=5, phrase_time_limit=4)

            word = r.recognize_google(audio)
            print(f"You said: {word}")

            if "jarvis" in word.lower():
                speak("Yes, how can I help you?")

                # Listen for the actual command
                with sr.Microphone(device_index=mic_index) as source:
                    print("Jarvis Active... Speak your command")
                    r.adjust_for_ambient_noise(source, duration=0.4)
                    audio = r.listen(source, timeout=6, phrase_time_limit=5)

                command = r.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            # No speech detected — just continue listening silently
            pass
        except sr.UnknownValueError:
            print("Could not understand audio, try again...")
        except Exception as e:
            print(f"Error: {e}")

    
# ====================== AI PROCESS ======================

aiProcess()

# ====================== PROCESS COMMAND ======================

processCommand()