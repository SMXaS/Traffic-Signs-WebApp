""" Virtual Bot Text to Speech Convertions """
from gtts import gTTS
from playsound import playsound
import os

# Language of speech
language = 'en'

# Intro
welcome_text = "Welcome to the Traffic Signs System"

# End
goodbye_text = "See you later, thank you for learning!"

# Welcome text convertion
output = gTTS(text=welcome_text, lang=language, slow=False)

# Save welcome to audio
output.save("welcome.mp3")

# Goodbye text convertion
output = gTTS(text=goodbye_text, lang=language, slow=False)

# Save goodbye to audio
output.save("goodbye.mp3")

# Testing with audio play of welcome text
os.system("start welcome.mp3")

# Testing with audio play of goodbye text
os.system("start goodbye.mp3")