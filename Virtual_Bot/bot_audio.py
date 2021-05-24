""" Virtual Bot Text to Speech Convertions """
from gtts import gTTS
import os


# Language of speech
language = 'en'


# Welcome text
welcome_text = "Welcome to the Traffic Signs System"


# Welcome text convertion
output = gTTS(text=welcome_text, lang=language, slow=False)


# Save welcome to audio
output.save("welcome.mp3")


# End
goodbye_text = "See you later, thank you for learning!"


# Goodbye text convertion
output = gTTS(text=goodbye_text, lang=language, slow=False)


# Save goodbye to audio
output.save("goodbye.mp3")


# Show Stop sign
show_signs_stop = "Can you please show me stop sign?"


# Stop sign text convertion
output = gTTS(text=show_signs_stop, lang=language, slow=False)


# Save stop sign request to audio
output.save("stop_sign.mp3")


# Show Stop sign
show_signs_oneWay = "Can you please show me one way sign?"


# One way sign text convertion
output = gTTS(text=show_signs_oneWay, lang=language, slow=False)


# Save one way sign request to audio
output.save("one_way_sign.mp3")


# Testing with audio play of welcome text
os.system("start welcome.mp3")


# Testing with audio play of goodbye text
os.system("start goodbye.mp3")
