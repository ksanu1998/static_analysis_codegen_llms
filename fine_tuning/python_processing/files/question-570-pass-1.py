def matchPattern(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == 'a' and s[i+1] == 'b':
            i += 2
        elif s[i] == 'b' and s[i+1] == 'a':
            i += 2
        else:
            return False
    return True
