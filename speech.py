
import speech
import time

response = speech.input("Say something, please.")
speech.say("You said " + response)

def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speech.say(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
'''
import string
import speech

while True:
    print "Talk:"
    phrase = speech.input()
    speech.say("You said %s" % phrase)
    print "You said {0}".format(phrase)
    #if phrase == "turn off":
    if phrase.lower() == "goodbye":
        break

'''


