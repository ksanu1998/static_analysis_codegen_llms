def checkString(s):
    Len = len(s)
    first = len(s) + 1
    for i in range(Len):
        if (s[i] == '1'):
            first = i
            break
    last = 0
    for i in range(Len - 1, -1, -1):
        if (s[i] == '1'):
            last = i
            break
    for i in range(first, last + 1):
        if (s[i] == '0'):
            return False
    return True


s = "00011111111100000"
if (checkString(s)):
    print("VALID")
else:
    print("NOT VALID")
