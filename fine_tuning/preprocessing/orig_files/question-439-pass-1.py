def getMaxRec(string, i, n, lookup):
    if i >= n:
        return 0
    if lookup[i] != -1:
        return lookup[i]
    ans = 1 + getMaxRec(string, i + 1, n, lookup)
    if i + 1 < n:
        if string[i] != string[i + 1]:
            ans = max(4 + getMaxRec(string, i + 2, n, lookup), ans)
        else:
            ans = max(3 + getMaxRec(string, i + 2, n, lookup), ans)
    lookup[i] = ans
    return ans


def getMaxWeight(string):
    n = len(string)
    lookup = [-1] * (n)
    return getMaxRec(string, 0, len(string), lookup)


if __name__ == "__main__":
    string = "AAAAABB"
    print("Maximum weight of a transformation of",
          string, "is", getMaxWeight(string))
