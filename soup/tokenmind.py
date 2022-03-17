import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words("hungarian"))

file = open("prompts.txt", "r", encoding='utf8')


tartalom = file.readlines()
tokens=[]
filtered_tokens=[]
filtered_all=[]

for mondat in tartalom:
    tokens.append(nltk.word_tokenize(mondat))

for mondat in tokens:
    for szo in mondat:
        if szo.casefold() not in stop_words and szo != ':':
            filtered_tokens.append(szo)
    filtered_all.append(filtered_tokens)
    filtered_tokens=[]
        

with open('xddd.txt', 'w', encoding='utf8') as f:
    for token in filtered_all:
        f.write(str(token)+'\n')

