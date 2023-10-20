import speech_recognition as sr


inputloc = "/Users/troyperment/Development/DataFiles/input/"
outputloc = "/Users/troyperment/Development/DataFiles/output/"

filename = "harvard"
extention = ".wav"

# initialize the recognizer
r = sr.Recognizer()
#
# open the file
with sr.AudioFile(inputloc + filename + extention) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    #text2 = r.recognize_tensorflow (audio_data)
    print(text)
    #print(text2)
