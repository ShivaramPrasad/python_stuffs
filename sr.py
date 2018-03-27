
'''
#audio to data
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:        # use the default microphone as the audio source
    audio = r.listen(source)   # listen for the first phrase and extract it into audio data

try:	
    print("You said " + r.recognize(audio)) 
# recognize speech using Google Speech Recognition
except LookupError:                    # speech is unintelligible
    print("Could not understand audio")
'''

#Transcription
import speech_recognition as sr

def hi():
	r = sr.Recognizer()
with sr.Microphone as source:
	print("Say something!")              
	audio = r.listen(source)                        

try:
	print("Transcription: " + r.recognize(audio))   
except LookupError:                                 
	print("Could not understand audio")

'''
#background microphone
import speech_recognition as sr
def callback(recognizer, audio):            # this is called from the background thread
    try:
        print("You said " + recognizer.recognize(audio)) 
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)                        
'''





if '__name__' == '__main__':
	hi()
