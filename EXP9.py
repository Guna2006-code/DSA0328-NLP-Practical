import re
words=["running","played","cats"]
for w in words:
    if re.search("ing$",w): t="VBG"
    elif re.search("ed$",w): t="VBD"
    else: t="NN"
    print(w,"->",t)
