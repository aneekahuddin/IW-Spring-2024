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
audiobook_files["test book one"] = "AudioBooks/goldilocks-shorter.mp3"

from gtts import gTTS 
import os
import cv2 
import random

def audiobook(): 
    cam_port = 0
    cap = cv2.VideoCapture(2) # connects to my iPhone camera currently
    os.system("afplay AudioInstructions/audiobookScanInstruction.mp3")
    
    audiobook_filename = ""
    # have them press a button when they are ready to read aloud
    option = input("scan title")
    if option == "1":
        ret, img = cap.read() 

        # saving the image 
        cv2.imwrite("img1.png", img) 
        cap.release() 

        #audiobook_title = detect_text("img1.png")
        audiobook_title = "test book one"
        audiobook_filename = audiobook_files[audiobook_title]
    if option == "2":
        audiobook_filename = random.choice(list(audiobook_files.values()))
        
    os_cmd = "afplay " + audiobook_filename
    os.system(os_cmd)
    print("here")


    cv2.destroyAllWindows() 

'''EXT - Have the book start at where it might have left off in previous cases, have the ability to skip forward in the story, etc.'''