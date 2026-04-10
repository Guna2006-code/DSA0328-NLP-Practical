import random
text="I love NLP and I love Python"
w=text.split()
pairs=[(w[i],w[i+1]) for i in range(len(w)-1)]
d={}
for a,b in pairs: d.setdefault(a,[]).append(b)

word="I"
for _ in range(5):
    print(word,end=" ")
    word=random.choice(d.get(word,w))
