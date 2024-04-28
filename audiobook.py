'''Audiobook:

Bot asks kid to hold the book in front of the camera. 

Camera waits until book is detected. Mic waits to hear a command from kid.

Once book is detected or a book title is mentioned, bot will take a image and will tell kid, “Processing”

Once the image/speech is processed, the Bot will confirm the book title.

The audiobook file is then played. 

If the audiobook is not starting from the first few seconds, then the bot will ask if they should start from the beginning or the current spot. 

Audiobook file Ends:

Bot tells kid the book is over. Then, recommends next set of books or encourages kid to read more. 

Bot logs this book (To send out to parents, To create a post reading list, to allow for rates, etc. )'''


audiobook_files = dict()
# Code Cleanup - Find a way to generate audiobook library in a better way
audiobook_files["Goldilocks"] = "AudioBooks/goldilocks-shorter.mp3"
audiobook_files["Little Red Riding Hood"] = "AudioBooks/Little-red-riding-hood-even-shorter.mp3"
audiobook_files["Boy Who Cried Wolf"] = "AudioBooks/storynory-boy-who-cried-wolf.mp3"

from gtts import gTTS 
import os
import random

def audiobook(): 
    os.system("afplay AudioInstructions/audiobookScanInstruction.mp3")
    
    audiobook_filename = ""

    # have them press a button when they are ready to read aloud
    option = input("Press 1 to listen to Goldilocks, 2 for Little Red Riding Hood, and 3 for Boy Who Cried Wolf")
    if option == "0":
        audiobook_filename = random.choice(list(audiobook_files.values()))
    elif option == "1":
        audiobook_title = "Goldilocks"
        audiobook_filename = audiobook_files[audiobook_title]
    elif option == "2":
        audiobook_title = "Little Red Riding Hood"
        audiobook_filename = audiobook_files[audiobook_title]
    elif option == "2":
        audiobook_title = "Boy Who Cried Wolf"
        audiobook_filename = audiobook_files[audiobook_title]
  
    os_cmd = "afplay " + audiobook_filename
    os.system(os_cmd)
    print("here")
    option = input("scan") # build in a way to "wait" better. (maybe another loop that pauses? )

'''EXT - Have the book start at where it might have left off in previous cases, have the ability to skip forward in the story, etc.'''