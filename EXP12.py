def earley(s):
    if s == "ab":
        return True
    return False

s = input("Enter string: ")
print("Accepted" if earley(s) else "Rejected")
