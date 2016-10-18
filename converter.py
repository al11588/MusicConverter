import progressbar #progress bar library
import time #time library
from pydub import AudioSegment #converter library

def export(sound,timeremaining):
	sound = AudioSegment.from_file("test1.mp3") #test1.mp3 is being converted
	sound.export("new.mp3", format="mp3", bitrate="128k") #new.mp3 is what it is going to be converted to.

timeremaining = progressbar.ProgressBar() #outputs the time remaining to get converted.
for i in timeremaining(range(80)):
    time.sleep(0.01)
