import pyttsx
'''
engine = pyttsx.init()
engine.say('hi am shiva .. whats your name')
engine.runAndWait()
'''

engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)

gender = engine.getproperty('voice')
engine.setproperty('voice', female)
'''
voice = pyttsx.voice.Voice()
voice.setproperty('gender', female)
#engine.setProperty('female', voices[65].id)
'''

#engine.setProperty('voice', voices[67].id) #change index to change voices

engine.say("Hi there, how's you ?")
engine.say("A B C D E F G H I J K L M")
engine.say("N O P Q R S T U V W X Y Z")
engine.say("0 1 2 3 4 5 6 7 8 9")
engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
engine.say("Violet Indigo Blue Green Yellow Orange Red")
engine.say("Apple Banana Cherry Date Guava")

engine.runAndWait()
