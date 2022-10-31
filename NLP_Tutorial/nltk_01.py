''''
'''
#import nltk
#nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Dr. Strange loves Ha noi. David loves chat of HCM city"

print("===== sent_tokenize: ")
tokens = sent_tokenize(text)
for token in tokens:
    print(token)

print("===== word_tokenize: ")
words = word_tokenize(text)
for word in words:
    print(word)

