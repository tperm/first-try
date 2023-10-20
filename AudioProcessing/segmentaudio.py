from pydub import AudioSegment

song = AudioSegment.from_wav("/Users/troyperment/Development/DataFiles/input/2023-09-10_123718_000.wav")

# PyDub handles time in milliseconds
one_minutes = 1 * 60 * 1000

first_1_minutes = song[:one_minutes]
filename = '/Users/troyperment/Development/DataFiles/output/Peter_1.wav' + i + '.wav'
first_1_minutes.export("/Users/troyperment/Development/DataFiles/output/Peter_1.wav", format="wav")