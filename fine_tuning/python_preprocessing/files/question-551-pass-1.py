def isTwoAlter(s):
    if len(s) < 2:
        return False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True
