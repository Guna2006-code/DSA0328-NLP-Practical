from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "playing", "easily", "studies"]

for word in words:
    print(word, "->", ps.stem(word))
