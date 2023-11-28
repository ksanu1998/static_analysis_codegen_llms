MAX_CHAR = 256


def isPresent(s, q):
    for i in range(len(s)):
        if s[i] in q:
            return True
    return False
