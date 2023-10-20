import pydub
inputloc = "/Users/troyperment/Development/DataFiles/input/"
outputloc = "/Users/troyperment/Development/DataFiles/output/"

filename = "Jinterview"
sound = pydub.AudioSegment.from_wav(inputloc + filename + ".wav")
sound.export(outputloc + filename + ".mp3", format="mp3")
print('done') 