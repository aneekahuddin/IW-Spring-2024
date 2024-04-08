'''In prototype, we will have a camera in the companion application that will allow the kid to “position” the book. 
They will click a button in the app to “Read Page Aloud”

With image data, call Vision Language Model to translate image data to text data. 

With the text data, call the Text to Speech Model to translate the text data to an audio file. 

Play the audio file. 

Resume to “scanning step”

To end the session, kid uses a voice command. (P - select on companion app) Returns to Ready to Read.

If there has not been a a command in 5+ minutes during the “scanning step” this will end the session.
'''

from gtts import gTTS 
import os
import cv2 

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
    return texts[0].description

    '''for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))'''

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

# set up camera:
def realTimeReading():
    cam_port = 0
    cap = cv2.VideoCapture(0) # connects to my iPhone camera currently
    os.system("afplay AudioInstructions/firstScanInstruction.mp3")

    # have them press a button when they are ready to read aloud
    option = input("scan")
    while True :
        '''ret, img = cap.read()  Trying to get there to be real time video so kid can set book properly in front of animal without guessing

        # Display the resulting frame 
        cv2.imshow('frame',img) 
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            break'''
        
        if option == "1":
            # capturing the single frame image 
            ret, img = cap.read() 

            # saving the image 
            cv2.imwrite("img1.png", img) 
            cv2.imshow("page", img) 
            k = cv2.waitKey(30) & 0xff
            if k == 27: 
                break

            page_text = detect_text("img1.png")
            readAloudSound = gTTS(text = page_text, lang = "en", slow = False)
            readAloudSound.save("AudioInstructions/readAloud.mp3")

            os.system("afplay AudioInstructions/readAloud.mp3")

            print("here")
        if option == "X" or option =="x":
            os.system("afplay AudioInstructions/endSessionInstruction.mp3")
            exit()
        
        #os.system("afplay additionalScanInstruction.mp3")
        option = input("next scan")

    cap.release() 
    cv2.destroyAllWindows() 


