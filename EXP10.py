words=["run","running"]
tags=["NN","NN"]

for i in range(len(words)):
    if words[i].endswith("ing"):
        tags[i]="VBG"

print(list(zip(words,tags)))
