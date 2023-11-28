def isVowel(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        return True
    return False


def createAltStr(str1, str2, start, l):
    finalStr = ""
    i = 0
    for j in range(start, l):
        finalStr = (finalStr + str1[i]) + str2[j]
        i + 1
    return finalStr


def findAltStr(str1):
    nv = 0
    nc = 0
    vstr = ""
    cstr = ""
    l = len(str1)
    for i in range(0, l):
        if (isVowel(str1[i])):
            nv += 1
            vstr = vstr + str1[i]
        else:
            nc += 1
            cstr = cstr + str1[i]
    if (abs(nv - nc) >= 2):
        return "no such string"
    if (nv > nc):
        return (vstr[0] + createAltStr(cstr, vstr, 1, nv))
    if (nc > nv):
        return (cstr[0] + createAltStr(vstr, cstr, 1, nc))
    if (cstr[0] < vstr[0]):
        return createAltStr(cstr, vstr, 0, nv)
    return createAltStr(vstr, cstr, 0, nc)


if __name__ == "__main__":
    str1 = "geeks"
    print(findAltStr(str1))
