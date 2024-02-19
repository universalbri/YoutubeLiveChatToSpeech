# Requirements:
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
# pip install pyttsx3
# https://pypi.org/project/pytchat/
# pip install pytchat

import pytchat
import pyttsx3 
import sys
 
def SpeakText(command):
    # Initialize the engine
    engine.say(command) 
    engine.runAndWait()

# total arguments
n = len(sys.argv)
if n == 2:
    # video id = HGOiuQUwqEw
    id = f"{sys.argv[1]}"
    chat = pytchat.create(video_id=id)
    engine = pyttsx3.init()

    while chat.is_alive():
        for c in chat.get().sync_items():
            SpeakText( f"{c.author.name} said {c.message}" )
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
else:
    print(f"Usage: run <Live Youtube Video ID To Listen in on.")