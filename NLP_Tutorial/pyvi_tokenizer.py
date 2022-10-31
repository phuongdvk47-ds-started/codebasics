''''
'''
from pyvi import ViTokenizer, ViPosTagger, ViUtils

text = "Trường đại học bách khoa hà nội"
tokens = ViTokenizer.tokenize(text)

print("=========")
for token in tokens:
    print(token)

taggers = ViPosTagger.postagging(tokens)
print("=========")
for tagger in taggers:
    print(tagger)
print("=========")
t1 = ViUtils.remove_accents(text)
print(t1)
print("=========")
t2 = ViUtils.add_accents(text)
print(t2)
