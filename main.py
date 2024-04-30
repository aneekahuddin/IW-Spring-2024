'''Kid turns on the storyteller bot “body” (camera, mic, speakers) and downloads the “brain” companion application (desktop or mobile based)

Future iterations could have some “account” creation - to differentiate reading between kids or to save info somewhere.

Kid bluetooth connects the body to the brain, pairing complete

Ready to Read --> should lead to RealTime Reading or to Audiobook

Shuts off the system.
'''

from gtts import gTTS 
import os
import time
import keyboard
import realtimereading as rtr 
import audiobook as ab

# Check that Speaker and Camera are connected
# If not, Return Error

'''EXT 1: Create some sense of "account" registration - Storyteller Bot has a name/Kid has a name/profile'''

# In companion app, print/say(
    #"Hi! I'm Storyteller Bot! I can't wait to read with you.
    # If you'd like to listen to a book, press 1.
    # If you'd like to read a book, press 2. ")
    #use GTTS (https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e)
'''    EXT 1: Change the press instruction to be an emoji button w/ a companion app UI
       EXT 2: Add in Voice Commands - Using something like Siri or converting speech to text and running through GPT to decide what the kid wants
       - For Ext 2, think about different voice struggles kids might have
       EXT 3: Change GTTS to a more "human" voice'''


sBotIntro = "Hi! I'm Storyteller Bot! I can't wait to read with you. If you'd like to read a book, press one. If you'd like to listen to a book, press two. \nYour Option (Press Enter to Continue): "
os.system("afplay AudioInstructions/sBotIntro.mp3")
option = input(sBotIntro)
if option == "1":
    print("real time reading option")
    rtr.realTimeReading()
elif option == "2":
    print("audiobook option")
    ab.audiobook()
elif option == "x" or option == "X":
    print("done")
    exit()



# Have the above statement repeat every 30 seconds if no response. After 2 minutes, power off
# if 2, move to real time reading()
# if 1, move to audiobook()
# if X, move to power off.

# Power Off - exit() from program


