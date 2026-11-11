# Jarvis - Virtual Voice Assistant

A Python-based voice-controlled virtual assistant that listens for a wake word, processes voice commands, performs everyday tasks, and answers questions using OpenAI.

## Features

- **Wake Word Detection:** Activates when it hears "Jarvis".
- **Voice Recognition:** Recognizes spoken commands using Google Speech Recognition.
- **Text-to-Speech:** Responds through voice using pyttsx3.
- **AI Integration:** Uses OpenAI to answer questions and process commands that aren't handled by built-in functionality.
- **Website Automation:** Opens websites such as YouTube, Google, Facebook, Instagram, X, LinkedIn, and GitHub.
- **Music Playback:** Opens songs from a predefined YouTube music library.
- **News Updates:** Fetches the latest Indian headlines using NewsAPI and reads up to five headlines aloud.

## Project Structure

```text
Jarvis-Virtual-Assistant/
│
├── main.py
├── ai_process.py
├── utility_shack.py
├── speech.py
├── musicLibrary.py
├── api_keys.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** `api_keys.py` is intentionally excluded from the public repository.

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- OpenAI API
- NewsAPI
- Requests
- Webbrowser

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Jarvis-Virtual-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv env313
```

Activate it on Windows:

```bash
env313\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**Note:** PyAudio may require additional installation steps depending on your operating system.

### 4. Configure API Keys

Create a file named `api_keys.py` in the project root directory.

Add your credentials:

```python
newsapi = "YOUR_NEWSAPI_KEY"
openai_api_key = "YOUR_OPENAI_API_KEY"
```

Never share your API keys publicly.

### 5. Run Jarvis

```bash
python main.py
```

Make sure your microphone is connected and the microphone device index in `main.py` is configured correctly.

## Usage

1. Run `main.py`.
2. Wait for Jarvis to initialize.
3. Say "Jarvis" to activate the assistant.
4. Speak your command.
5. Jarvis processes the command and responds.

## Configuration

The microphone device index is configured in `main.py`:

```python
mic_index = 1
```

Change this value according to your microphone setup.

## Security

- API credentials are stored locally in `api_keys.py`.
- `api_keys.py` is excluded through `.gitignore`.
- Virtual environment files are not included in the repository.

## Future Improvements

- Improved command recognition and handling.
- Better error handling.
- Expanded music library.
- Additional automation features.
- Improved project architecture.

## License

This project is available for learning and educational purposes.
