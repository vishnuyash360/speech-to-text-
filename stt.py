import streamlit as st
import speech_recognition as sr

# Function to convert speech to text
def speech_to_text(language):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech in the chosen language
            text = recognizer.recognize_google(audio_data, language=language)
            st.write(f"You said: {text}")

        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            st.write(f"Could not process the request: {e}")

# Streamlit interface
st.title("Speech to Text Application")

# Language selection
language_choice = st.selectbox("Choose a language", ["English", "Hindi"])

# Map selection to language codes
if language_choice == "English":
    language = "en-IN"
elif language_choice == "Hindi":
    language = "hi-IN"

# Button to start recording
if st.button("Start Recording"):
    speech_to_text(language)
