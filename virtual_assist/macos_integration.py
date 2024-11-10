#Executes macos-specific commands based on intent

import os
from response import speak 

def execute_command(intent,command):
    if intent == "check_weather":
        from weather_api import get_weather
        city_name = extract_city_name(command)
        get_weather(city_name)
    elif intent == "open_application":
        app_name = command.split("open")[-1].strip()
        open_application(app_name)
    else:
        speak("Sorry, I can't do that yet.")

def open_application(app_name):
    os.system(f"osascript -e 'tell application \"{app_name}\" to activate'")
    speak(f"Opening {app_name}")

def extract_city_name(command):
    words = command.split()
    # Assuming the user says "weather in <city_name>"
    if "weather in" in command:
        start_index = words.index("in") + 1
        city_name = " ".join(words[start_index:])
        return city_name
    else:
        # Default city if no specific city is mentioned
        return "New Delhi"
