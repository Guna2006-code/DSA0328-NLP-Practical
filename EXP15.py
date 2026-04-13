def pcfg(s):
    if s == "ab":
        return "Accepted (0.9)"
    return "Rejected"

s = input("Enter string: ")
print(pcfg(s))
