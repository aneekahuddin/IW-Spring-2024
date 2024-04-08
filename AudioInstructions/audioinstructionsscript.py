from gtts import gTTS 

def createAudioInstructions(phrase, filename):
    language = "en"
    audio = gTTS(text = phrase, lang = language, slow = False)
    audio.save(filename + ".mp3")

createAudioInstructions("practice making something", "test")

sBotIntro = "Hi! I'm Storyteller Bot! I can't wait to read with you. If you'd like to listen to a book, press one. If you'd like to read a book, press two. \nYour Option (Press Enter to Continue): "

audiobookScanInstruction = "Storyteller Bot is ready to read with you! Pick a book and place it in front of my eyes. When you're ready, press 1 and enter to continue!"

firstScanInstruction = "Storyteller Bot is ready to read with you! Pick a book and place it in front of my eyes. When you're ready, press 1 and enter to continue!"
additionalScanInstruction = "To read another page, press 1 and enter to continue."
endSessionInstruction = "I loved reading with you! Let's read again next time."