def findNextGreaterNumber(n):
    res = ""
    a = ""
    b = ""
    aCount = 0
    bCount = 0

    for i in range(len(n)):
        if n[i].isdigit():
            if aCount == 0:
                a += n[i]
                aCount += 1
            else:
                b += n[i]
                bCount += 1
        else:
            res += n[i]

    if aCount == 0 or bCount == 0:
        return -1

    return int(res + str(int(b) + 1))
