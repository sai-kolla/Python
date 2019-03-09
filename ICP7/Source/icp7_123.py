import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import wordpunct_tokenize,pos_tag,ne_chunk

url = 'https://en.wikipedia.org/wiki/Google'
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")


f = open('Input.txt','w+',encoding="utf-8")
text = soup.get_text()
f.write(text)


f1 = open('Input.txt','r',encoding="utf-8")
data = f1.read()

#Tokentization
stokens = nltk.sent_tokenize(data)
wtokens = nltk.word_tokenize(data)

f3 = open('stokens.txt', 'w+',encoding = "utf-8")

print('!!!!!Tokenization!!!!!!')
for s in stokens:
    f3.write(s)

f4 = open('wtokens.txt', 'w+',encoding = "utf-8")

for w in wtokens:
    f4.write(w)

f5 = open('stemming.txt', 'w+',encoding = "utf-8")

print('!!!!!!!!!!!!!!!!!!Stemming!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#Stemming
lStemmer = LancasterStemmer()
for w in wtokens:
    f5.write(lStemmer.stem(w))

f6 = open('POS.txt', 'w+',encoding = "utf-8")

#POS
print('!!!!!!!!!!!!!!!!!!!!!!!!POS!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for w in wtokens:
    f6.write(str(nltk.pos_tag(nltk.word_tokenize(w))))

f7 = open('Lemmatizer.txt', 'w+',encoding = "utf-8")

#Lemmatizer
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!Lemmatizer!!!!!!!!!!!!!!!!!!!!!!!!')
lemmatizer = WordNetLemmatizer()
for w in wtokens:
    f7.write(lemmatizer.lemmatize(w))

f8 = open('Named_entry.txt', 'w+',encoding = "utf-8")

#Named entity recognition
print('!!!!!!!!!!!!!!!!!!Named Entity Recognition!!!!!!!!!!!!!!!!!!!!!!!!')
for s in stokens:
    f8.write(str(pos_tag(wordpunct_tokenize(s))))

f9 = open('Trigrams.txt', 'w+',encoding = "utf-8")

#trigrams
print('!!!!!!!!!!!!!!!!!!!!!!!Trigrams!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
tgram = ngrams(wtokens,3)
for t in tgram:
    f9.write(str(t))
