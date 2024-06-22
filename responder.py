import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech with a female voice
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    
    # Set properties for the female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Assuming index 1 corresponds to a female voice
    
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for the user to speak
while True:
    # Exception handling to handle exceptions at runtime
    try:
        # Use the microphone as a source for input
        with sr.Microphone() as source:
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio = r.listen(source)
        
        # Using Google to recognize audio
        recognized_text = r.recognize_google(audio).lower()
        print("You said:", recognized_text)
        
        # Check if the recognized text contains "hey lucia"
        if "hey lucy" in recognized_text:
            # Speak the recognized text with a female voice
            SpeakText(recognized_text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Could not understand audio")