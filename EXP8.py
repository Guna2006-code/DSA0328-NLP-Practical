words=["cats","run"]
tags={"cats":{"N":0.9},"run":{"V":0.8}}
for w in words:
    print(w,"->",max(tags.get(w,{"N":1}),key=tags.get(w,{"N":1}).get))
