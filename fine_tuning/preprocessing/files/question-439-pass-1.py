def getMaxRec(string, i, n, lookup):
    if i == n:
        return 0
    if lookup[i]!= -1:
        return lookup[i]
    lookup[i] = max(string[i] + getMaxRec(string, i + 2, n, lookup), getMaxRec(string, i + 1, n, lookup))
    return lookup[i]
