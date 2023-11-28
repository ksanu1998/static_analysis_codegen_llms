def merge(s1, s2):
    result = ""
    i = 0
    while (i < len(s1)) or (i < len(s2)):
        if (i < len(s1)):
            result += s1[i]
        if (i < len(s2)):
            result += s2[i]
        i += 1
    return result


s1 = "geeks"
s2 = "forgeeks"
print(merge(s1, s2))
