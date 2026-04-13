g = {"S": [["a","S","b"], []]}

def parse(s):
    if s == "":
        return True
    if s[0] == "a" and s[-1] == "b":
        return parse(s[1:-1])
    return False

s = input("Enter string: ")
print("Accepted" if parse(s) else "Rejected")
