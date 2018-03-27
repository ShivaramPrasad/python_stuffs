'''
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import httplib
import json
import sys

def speech_to_text(audio):
    url = "www.google.com"
    path = "/speech-api/v1/recognize?xjerr=1&amp;client=chromium&amp;lang=en"
    headers = { "Content-type": "audio/x-flac; rate=16000" };
    params = {"xjerr": "1", "client": "chromium"}
    conn = httplib.HTTPSConnection(url)
    conn.request("POST", path, audio, headers)
    response = conn.getresponse()
    data = response.read()
    jsdata = json.loads(data)
    return jsdata["hypotheses"][0]["utterance"]

if __name__ == "__main__":
    if len(sys.argv) != 2 or "--help" in sys.argv:
        print "Usage: stt.py "
        sys.exit(-1)
    else:
        with open(sys.argv[1], "r") as f:
            speech = f.read()
        text = speech_to_text(speech)
        print text
'''

# -*- coding: utf-8 -*-
from espeak import espeak

from datetime import datetime

t = datetime.now().strftime(“%k %M”)
espeak.synth(“You’re listening to Luke’s radio station. The time is %s”%t)

