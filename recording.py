import sounddevice as sd
import numpy as np

def hi():
	(fs1, x) = read('helloo.wav', 'rb')
	sd.play(x, fs1)
	sd.wait(10000000)


if '__name__' == '__main__':
	hi()
