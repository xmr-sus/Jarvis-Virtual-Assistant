import speech_recognition as sr
import pyttsx3

# ====================== INITIALIZATION ======================

recognizer = sr.Recognizer()
engine = pyttsx3.init()


# ====================== SPEAK FUNCTION ======================

def speak(text):
    """Convert text to speech using pyttsx3"""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
