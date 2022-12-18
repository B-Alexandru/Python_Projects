from gtts import gTTS  # Import the required module for text to speech conversion
import os  # This will import the os module


abc = open('sample.txt') # Open the text file in read mode

text = abc.read()  # Reading the text from the file

language = 'en' # The language in which you want to convert

obj = gTTS(text=text, lang=language, slow=False) # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed

obj.save("welcome.mp3") # Saving the converted audio in a mp3 file named welcome

os.system("welcome.mp3") # Playing the converted file