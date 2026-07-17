import speech_recognition as sr
from text_to_speech import speak

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_vosk(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Request error: {e}"

def main():
    while True:
        command = recognize_speech_from_microphone()
        print(f"You said: {command}")
        handle_command(command)

def handle_command(command):
    if "check my schemes" in command.lower():
        speak("Checking your eligibility...")
        # Call backend API to check eligibility and get results
    elif "read my eligible schemes" in command.lower():
        speak("Reading your eligible schemes...")
        # Read out the list of eligible schemes
    elif "search farmer schemes" in command.lower():
        speak("Searching farmer schemes...")
        # Search for farmer-related schemes
    elif "what documents are required" in command.lower():
        speak("What documents are required?")
        # List required documents
    elif "repeat" in command.lower():
        speak("Repeating the last statement...")
        # Repeat the last statement
    elif "go back" in command.lower():
        speak("Going back...")
        # Navigate back

if __name__ == "__main__":
    main()
