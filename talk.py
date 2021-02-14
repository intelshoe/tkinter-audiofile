'''
Main interface to features.

'''
import speech_recognition as sr
import time
from os import path

class Talk():
    def __init__(self):
        seconds = 5
        fname = ""

    def __str__():
        return "Talk Options"

    # saves audio to wav file and outputs speach to text
    def record(self, seconds, fname):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        time.sleep(seconds)
        # write audio to a WAV file
        with open(fname + ".wav", "wb") as f:
            f.write(audio.get_wav_data())

        # begin code to transcribe audio to text
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), fname + ".wav")
        # use the above audio file as the source to be translated to text
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            return ("I think I heard: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return ("Could not request results from Google Speech Recognition service; {0}".format(e))
