from gtts import gTTS 

def createAudioInstructions(phrase, filename):
    language = "en"
    audio = gTTS(text = phrase, lang = language, slow = False)
    audio.save(filename + ".mp3")

def text_to_speech(text: str, outfile: str) -> str:
    """Converts plaintext to SSML and
    generates synthetic audio from SSML

    Args:

    text: text to synthesize
    outfile: filename to use to store synthetic audio

    Returns:
    String of synthesized audio
    """
    from google.cloud import texttospeech
    import html
    # Replace special characters with HTML Ampersand Character Codes
    # These Codes prevent the API from confusing text with
    # SSML commands
    # For example, '<' --> '&lt;' and '&' --> '&amp;'
    escaped_lines = html.escape(text)

    # Convert plaintext to SSML in order to wait two seconds
    #   between each line in synthetic speech
    ssml = "<speak>{}</speak>".format(
        escaped_lines.replace("\n", '\n<break time="2s"/>')
    )

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Sets the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    # Builds the voice request, selects the language code ("en-US") and
    # the SSML voice gender ("MALE")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    # Selects the type of audio file to return
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Performs the text-to-speech request on the text input with the selected
    # voice parameters and audio file type

    request = texttospeech.SynthesizeSpeechRequest(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    response = client.synthesize_speech(request=request)

    # Writes the synthetic audio to the output file.
    with open(outfile, "wb") as out:
        out.write(response.audio_content)
        print("Audio content written to file " + outfile)

createAudioInstructions("practice making something", "test")

sBotIntro = "Hi! I'm Rhino Reader! I can't wait to read with you. If you'd like to read a book, press one. If you'd like to listen to a book, press two. \nYour Option (Press Enter to Continue): "
audiobookScanInstruction = "Rhino Reader is ready to read! You have Goldilocks, Little Red Riding Hood, and the Boy Who Cried Wolf in your library. Press 1 to listen to Goldilocks, 2 for Little Red Riding Hood, and 3 for Boy Who Cried Wolf."
firstScanInstruction = "Rhino Reader is ready to read with you! Pick a book and place it in front of my eyes. When you're ready, press 1 and enter to continue!"
additionalScanInstruction = "To read another page, press 1 and enter to continue."
endSessionInstruction = "I loved reading with you! Let's read again next time."

#createAudioInstructions(audiobookScanInstruction, "audiobookScanInstruction")

text_to_speech(sBotIntro, "sBotIntro.mp3")
text_to_speech(audiobookScanInstruction, "audiobookScanInstruction.mp3")
text_to_speech(firstScanInstruction, "firstScanInstruction.mp3")
text_to_speech(additionalScanInstruction, "additionalScanInstruction.mp3")
text_to_speech(endSessionInstruction, "endSessionInstruction.mp3")