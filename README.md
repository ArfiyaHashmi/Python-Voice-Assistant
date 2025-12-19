# Jerry - AI Voice Assistant 🎙️

A feature-rich Python-based voice assistant that can perform various tasks through voice commands, including playing music, fetching news, opening websites, and engaging in intelligent conversations using local AI models.

## ✨ Features

### Core Capabilities
- 🎤 **Voice Command Recognition** - Wake word activation with "Jerry"
- 🔊 **Text-to-Speech Responses** - Natural voice feedback using gTTS
- 🎵 **Music Playback** - Play songs from your custom library on YouTube
- 📰 **News Updates** - Fetch latest headlines from CNN, BBC, and Reuters RSS feeds
- 🌐 **Web Browser Integration** - Quick access to popular websites
- 🤖 **AI-Powered Conversations** - Local AI integration using Ollama (LLaMA 3.2)
- 🔄 **Fallback Response System** - Simple rule-based responses when AI is unavailable
- ⚡ **Real-time Processing** - Instant response to voice commands

### Supported Commands
- **Music**: "Play [song name]" - Plays music from YouTube
- **Websites**: "Open Google/Facebook/LinkedIn/YouTube"
- **News**: "News" - Reads latest headlines
- **General Questions**: Ask anything for AI-powered responses
- **Time/Date**: Ask for current time or date
- **Jokes**: Request a joke for entertainment

## 🛠️ Technology Stack

### Python Libraries
- **SpeechRecognition** - Voice command capture and processing
- **gTTS (Google Text-to-Speech)** - Natural voice synthesis
- **pyttsx3** - Offline text-to-speech engine
- **pygame** - Audio playback management
- **requests** - API communication
- **webbrowser** - Web integration

### External Services
- **Google Speech Recognition API** - Voice-to-text conversion
- **RSS2JSON API** - News feed aggregation
- **Ollama** - Local LLM for AI responses (optional)

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Microphone for voice input
- Internet connection for online features
- Speakers/headphones for audio output

### Python Dependencies
```
SpeechRecognition>=3.10.0
pyttsx3>=2.90
requests>=2.31.0
gTTS>=2.3.0
pygame>=2.5.0
```

### Optional
- **Ollama** with LLaMA 3.2:1b model (for enhanced AI responses)

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/jerry-voice-assistant.git
cd jerry-voice-assistant
```

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install PyAudio (Required for SpeechRecognition)

**For Windows:**
```bash
pip install pyaudio
```

**For macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**For Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-pyaudio
pip install pyaudio
```

### Step 4: Install Ollama (Optional - for AI features)

Visit [Ollama's website](https://ollama.ai/) and follow installation instructions, then pull the model:
```bash
ollama pull llama3.2:1b
```

## 🎯 Usage

### Starting Jerry
```bash
python main.py
```

### Interaction Flow
1. **Wait for the wake word**: Say "Jerry" to activate the assistant
2. **Wait for confirmation**: Jerry will respond with "Yes?"
3. **Speak your command**: Clearly state what you want Jerry to do
4. **Get response**: Jerry will process and respond to your command

### Example Conversations

```
You: "Jerry"
Jerry: "Yes?"
You: "Open YouTube"
Jerry: "Opening YouTube."

---

You: "Jerry"
Jerry: "Yes?"
You: "Play Love Story"
Jerry: "Playing Love Story."

---

You: "Jerry"
Jerry: "Yes?"
You: "News"
Jerry: "Here are a few headlines from CNN..."

---

You: "Jerry"
Jerry: "Yes?"
You: "What time is it?"
Jerry: "The current time is 3:45 PM"
```

## 📁 Project Structure

```
jerry-voice-assistant/
│
├── main.py              # Main application with voice processing
├── musicLibrary.py      # Music database with YouTube links
├── trail.py             # Testing script for pyttsx3
├── .gitignore          # Git ignore rules
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🎵 Music Library

Currently includes three pre-configured songs in `musicLibrary.py`:
- **Love Story** - Taylor Swift
- **August** - Taylor Swift  
- **Perfect** - Ed Sheeran

### Adding More Songs
Edit `musicLibrary.py` and add entries in this format:
```python
music = {
    "song_name": "https://youtube.com/watch?v=VIDEO_ID",
    # Add more songs here
}
```

## 🔧 Configuration

### Adjusting Voice Settings
In `speak()` function, you can modify:
- Voice speed
- Volume
- Language (default: English)

### Customizing Wake Word
Change the wake word in `main.py`:
```python
if "jerry" in wake_word:  # Replace "jerry" with your preferred wake word
```

### Timeout Settings
Adjust listening timeouts in `main.py`:
```python
audio = r.listen(source, timeout=3, phrase_time_limit=2)  # Modify values as needed
```

## 🤖 AI Features

### With Ollama (Recommended)
- Context-aware responses
- Natural conversations
- Personality customization
- Offline AI processing

### Without Ollama (Fallback Mode)
- Rule-based responses
- Basic queries (time, date, jokes)
- Limited conversational ability

## 📰 News Sources

Jerry fetches news from multiple RSS feeds:
1. **CNN** - International news
2. **BBC** - World news
3. **Reuters** - Top news

The system automatically tries multiple sources if one fails.

## 🐛 Troubleshooting

### Common Issues

**"Microphone not found"**
- Check if your microphone is properly connected
- Ensure microphone permissions are granted to Python
- Test with `trail.py` to verify audio output

**"Speech Recognition error"**
- Check internet connection (required for Google Speech API)
- Speak clearly and wait for the "Listening..." prompt
- Reduce background noise

**"Ollama connection failed"**
- Ensure Ollama is installed and running
- Verify the model is pulled: `ollama list`
- Check if the service is running: `ollama serve`

**"Module not found"**
- Reinstall dependencies: `pip install -r requirements.txt`
- Use a virtual environment to avoid conflicts

**Audio playback issues**
- Ensure pygame mixer is properly initialized
- Check system audio settings
- Verify `temp.mp3` is being created and deleted

## 🔒 Privacy & Security

- Voice commands are processed using Google's Speech Recognition API
- When using Ollama, AI processing happens locally on your machine
- No conversation data is stored permanently
- Temporary audio files are automatically deleted after playback

## 🚀 Future Enhancements

Planned features for future versions:
-  Spotify integration for music playback
-  Weather updates with location detection
-  Calendar and reminder management
-  Email reading and sending
-  Smart home device control
-  Multi-language support
-  Custom voice profiles
-  Conversation history logging (optional)
-  Web search integration
-  File system operations

### Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation for new features

## 👨‍💻 Author

Developed as a demonstration of:
- Python programming expertise
- Natural Language Processing (NLP)
- API integration and management
- Real-time audio processing
- Modular software architecture
- AI/ML integration with local models

## 🙏 Acknowledgments

- **Google Speech Recognition** - For voice-to-text conversion
- **Ollama** - For local LLM hosting
- **gTTS** - For natural text-to-speech
- **RSS2JSON** - For news feed aggregation
- Open-source community for various libraries


### Quick Start Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run the assistant
python main.py

# Test audio output
python trail.py
```

**Made with ❤️ using Python**
