# TEXT-AUDIO TRANSCRIPTION USING THE GTTS LIBRARY

# STEP 1: Download/import transcription package
from gtts import gTTS
import os
import re

# STEP 2: Select file and open file and save content to variable
fpath = './gdpr.txt'
f = open(fpath, 'r')
content = f.read()
content = re.sub(r'\s+',' ',content)

# STEP 4: Convert content to audio file and select language
language = 'en'
myobj = gTTS(text=content[:200],
             lang=language,
             tld='ie',
             slow=False)

# STEP 5: Save mp3 to director and close txt file
myobj.save('gdpr_short.mp3')
f.close()

# FIN

# NOTES
# Documentation for gtts: https://gtts.readthedocs.io/en/latest/module.html
# Using conda? Here you go. conda install -c conda-forge gtts
# Want to compress the file? "Check out Simple Audio Compression With Python"
# Medium, url 'https://medium.com/@jmpion/simple-audio-compression-with-python-70bdd7535b0a'