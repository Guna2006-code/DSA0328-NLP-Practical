import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The cats are running in the garden"

words = word_tokenize(text)
tags = pos_tag(words)

for word, tag in tags:
    print(word, "->", tag)
