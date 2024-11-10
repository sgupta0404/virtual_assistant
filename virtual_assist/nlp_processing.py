#Process the command to determine the intent

import spacy
nlp= spacy.load("en_core_web_sm")

#Function uses keyword matching to determine the type of command
def identify_intent(command):
    command=command.lower()
    if "weather" in command:
        return "check_weather"
    elif "open" in command:
        return "open_application"
    else:
        return "unknown_intent"
    