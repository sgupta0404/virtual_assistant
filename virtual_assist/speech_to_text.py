#To convert audio input from mic to text

import speech_recognition as sr

def get_audio_input():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio=recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
