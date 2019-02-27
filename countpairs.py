import re
import sys
from collections import Counter
FILE_NAME = str(sys.argv[1]) 
words = re.findall('\w+', open(FILE_NAME,'r', encoding ='utf-8', errors= 'ignore').read())
print(Counter(zip(words,words[1:])))
