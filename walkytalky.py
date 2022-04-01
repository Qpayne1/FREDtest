#program to make brother FRED talk

import speech_recognition as sr
import pyttsx3

#initialize recognizer
r=sr.Recognizer()

#speech to text conversion function
def SpeakText(command):

    #initialize text to speech
    text_speech = pyttsx3.inti()
    text_speech.say(command)
    text_speech.runAndWait()

#allow user to speak
while(1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print('Did you say '+MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))
    except sr.UnknownValueError:
        print('unknown error occurred')
