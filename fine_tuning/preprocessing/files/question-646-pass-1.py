MAX_CHARS = 256


def areIsomorphic(string1, string2):
    if len(string1)!= len(string2):
        return False
    if len(string1) == 0:
        return True
    if string1[0]!= string2[0]:
        return False
    for i in range(1, len(string1)):
        if string1[i]!= string2[i]:
            return False
    return True
