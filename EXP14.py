def check(s):
    w = s.split()
    if w[0] == "He" and w[1].endswith("s"):
        return "Correct"
    if w[0] == "They" and not w[1].endswith("s"):
        return "Correct"
    return "Wrong"

s = input("Enter sentence: ")
print(check(s))
