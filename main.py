import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import json
import re #regular expressions - cleaning newsheadlines
from gtts import gTTS
import pygame
import os


# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak_old(text):
    """Converts text to speech and plays it."""
    engine.say(text)
    engine.runAndWait()

def speak (text):
     tts = gTTS(text)
     tts.save('temp.mp3')
     
     #initialize pygame mixer
     pygame.mixer.init()

     #load the mp3 file
     pygame.mixer.music.load('temp.mp3')

     #play the loaded music
     pygame.mixer.music.play()

     #keep the program running until the music stops playing
     while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)
     
     pygame.mixer.music.unload()
     os.remove("temp.mp3")     

def get_free_ai_response(prompt):
    """
    Uses a free local AI service (Ollama) to get a response.
    Requires Ollama to be installed and running with a model pulled.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": f"You are Jarvis, a helpful AI assistant. User says: {prompt}",
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 100 
                }
            },
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()

            ai_response = result.get("response", "").strip()
            
            # The model might start with its persona, so we clean it up
            if ai_response.startswith("you are Jarvis, a helpful AI assistant."):
                ai_response = ai_response.split("assistant.")[-1].strip()
            
            return ai_response if ai_response else "I'm not sure how to respond to that."
        else:
            print(f"Ollama API error: {response.status_code}")
            return "I'm having trouble thinking right now."
            
    except requests.exceptions.ConnectionError:
        # If Ollama is not running, use a simple fallback
        print("Ollama is not running. Using simple response mode.")
        return get_simple_response(prompt)
    except Exception as e:
        print(f"AI service error: {e}")
        return get_simple_response(prompt)

def get_simple_response(prompt):
    """Simple rule-based responses for common queries when AI is unavailable."""
    prompt = prompt.lower()
    
    if any(word in prompt for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you today?"
    
    elif any(word in prompt for word in ["time", "what time"]):
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    elif any(word in prompt for word in ["date", "today"]):
        from datetime import datetime
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date}"
    
    elif any(word in prompt for word in ["weather"]):
        return "I'd love to check the weather for you, but I need a weather API key to do that."
    
    elif any(word in prompt for word in ["joke", "funny"]):
        import random
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        return random.choice(jokes)
    
    elif any(word in prompt for word in ["thanks", "thank you"]):
        return "You're welcome! Happy to help."
    
    elif any(word in prompt for word in ["bye", "goodbye", "exit"]):
        return "Goodbye! Have a great day!"
    
    else:
        return "I heard you say something, but I'm not sure how to help with that. Try asking me to open a website, play music, or get news."

def get_rss_news():
    """Get news from free RSS feeds."""
    try:
        rss_sources = [
            "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Frss.cnn.com%2Frss%2Fedition.rss",
            "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Ffeeds.bbci.co.uk%2Fnews%2Frss.xml",
            "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Ffeeds.reuters.com%2Freuters%2FtopNews"
        ]
        
        for source_url in rss_sources:
            try:
                response = requests.get(source_url, timeout=8)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
                data = response.json()
                
                if data.get('status') == 'ok' and data.get('items'):
                    items = data['items'][:3] # Get top 3 headlines
                    feed_title = data.get('feed', {}).get('title', 'News')
                    speak(f"Here are a few headlines from {feed_title}")
                    
                    for i, item in enumerate(items, 1):
                        title = item.get('title', 'No title').strip()
                        # Clean up title (remove HTML tags and extra whitespace)
                        title = re.sub('<[^<]+?>', '', title)
                        
                        print(f"{i}. {title}")
                        speak(title)
                        time.sleep(0.5) # Shorter pause between headlines
                    return  # Exit function after successfully getting news
                
            except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
                print(f"Error with source {source_url}: {e}")
                continue
        
        # If all sources failed
        speak("Sorry, I couldn't fetch news from any source right now.")
            
    except Exception as e:
        speak("News service is currently unavailable.")
        print(f"RSS News error: {e}")

def processCommand(c):
    """Processes the spoken command and performs the corresponding action."""
    c = c.lower()
    
    if "open google" in c:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        speak("Opening Facebook.")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn.")
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in c:
        speak("Opening YouTube.")
        # Corrected URL for YouTube
        webbrowser.open("https://youtube.com")

    elif "news" in c:
        print("Fetching latest news...")
        get_rss_news()

    elif c.startswith("play"):
        song = c.replace("play", "", 1).strip().lower()
        if song:
            print("Requested song:", song)
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                speak(f"Playing {song}.")
                webbrowser.open(link)
            else:
                speak(f"I couldn't find the song {song} in your library.")
                print(f"'{song}' not found in musicLibrary.")
        else:
            speak("Please specify the song name after 'play'.")
    else:
        # For all other commands, use the AI assistant
        response = get_free_ai_response(c)
        speak(response)
        print("AI Response:", response)


if __name__ == "__main__":
    speak("Hey! This is Jerry, How can i help you...")
    
    # Check if Ollama is available
    try:
    # This checks if a specific model exists and is ready
        test_response = requests.get("http://localhost:11434/api/show", json={"name": "llama3.2:1b"}, timeout=10)
        if test_response.status_code == 200:
            speak("Local AI model detected and ready.")
        else:
            speak("Using simple response mode.")
    except requests.exceptions.RequestException:
        speak("Using simple response mode. For better AI, install Ollama")
    
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for a short phrase for the wake word
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                wake_word = r.recognize_google(audio).lower()
                print("Heard:", wake_word)

            if "jerry" in wake_word:
                speak("Yes?")
                print("Yes?")
                
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    # Listen for a longer command
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio).lower()
                    print("Command:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
        except KeyboardInterrupt:
            speak("Shutting down Serri. Goodbye!")
            break
            
    print("Jerry offline.")