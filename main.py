# main.py

from speech_to_text import get_audio_input
from nlp_processing import identify_intent
from macos_integration import execute_command
from weather_api import get_weather
from response import speak

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = get_audio_input()
        if command:
            intent = identify_intent(command)
            if intent:
                execute_command(intent, command)

if __name__ == "__main__":
    main()
