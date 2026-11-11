from api_keys import openai_api_key  # Import the OpenAI API key from api_keys.py
from openai import OpenAI

def aiProcess(command):
    """Send command to OpenAI and get response"""
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Keep answers short and clear."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I faced an error while processing: {e}"
