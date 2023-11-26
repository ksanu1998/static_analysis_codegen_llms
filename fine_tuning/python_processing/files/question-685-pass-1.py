def createPrefixArray(n, arr, prefSize, pref):
    for i in range(1, n):
        pref[i] = pref[i - 1] + arr[i]
    return pref
