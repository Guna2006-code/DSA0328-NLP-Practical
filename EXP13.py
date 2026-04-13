def tree(s):
    if s == "ab":
        return "(S (A a) (B b))"
    return "Invalid"

s = input("Enter string: ")
print(tree(s))
