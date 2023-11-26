def trickyCase(s, index):
    if s[index] % 2 == 0:
        return s[index]
    else:
        return trickyCase(s, index + 1)
