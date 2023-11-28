def checkPattern(string, pattern):
    for i in range(len(string)):
        if string[i]!= pattern[i % len(pattern)]:
            return False
    return True
