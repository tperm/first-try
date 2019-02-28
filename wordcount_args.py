import re
import sys
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
FILE_NAME = str(sys.argv[1]) 
WORD_GROUPS = int(sys.argv[2])

stopWords = set(stopwords.words('english'))
wordsFiltered = []

words = re.findall('\w+', open(FILE_NAME,'r', encoding ='utf-8', errors= 'ignore').read().lower())
#print(Counter(zip(words)))
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
        
if WORD_GROUPS == 1:
    text = str((Counter(zip(wordsFiltered,))))
elif WORD_GROUPS == 2:
    text = str((Counter(zip(wordsFiltered,wordsFiltered[1:]))))
elif WORD_GROUPS == 3:
    text = str((Counter(zip(wordsFiltered,wordsFiltered[1:],wordsFiltered[2:]))))
#text =str((Counter(zip(words,))))
text = (text.replace(", (","|").replace(" ","").replace("'",""))
text = (text.replace(","," ").replace(")",""))
text = (text.replace(":",","))
finaltext = text.split('|')
for text in finaltext:
	print(text)
