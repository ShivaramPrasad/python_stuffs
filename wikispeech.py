import json
#import speech_recognisition as sr
import wikipedia
import time
#import pyttsx
# -*- coding: utf-8 -*-
from espeak import espeak
espeak.set_voice("female3")
import getch
from getch import getch, pause


 
#query = speech.input("say something, please...")

espeak.synth("say something")
query = raw_input("say something .. ")
print("Info ~ \nPLEASE WAIT...\n")
espeak.synth("please wait")

#for line in query:
try:	
	#engine = pyttsx.init()
	print(wikipedia.summary(query, sentences = 4))
	espeak.synth(repr(wikipedia.summary(query, sentences = 4)))
	pause()
		
	#engine.runAndWait()
	print("\n")
	
except wikipedia.exceptions.DisambiguationError as e:
	print("\n[ - ] there are many suggestion about this word .. please mention properly.\n")
	print("But don't worry i will help you.. \n")
	search = query
	time.sleep(2)
	print(wikipedia.search(search))
	print(">>these are my suggestions..")
	search_result = raw_input("\nNow which <{}> suggestion do you need.. ".format(search))
	print("\n"+wikipedia.summary(search_result, sentences = 4))
#speech.say(wikipedia.summary(query, sentences = 4))




