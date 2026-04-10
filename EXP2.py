def ends_with_ab(s):
    state = 0

    for char in s:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    return state == 2
string = "aab"

if ends_with_ab(string):
    print("Accepted (ends with 'ab')")
else:
    print("Rejected")
