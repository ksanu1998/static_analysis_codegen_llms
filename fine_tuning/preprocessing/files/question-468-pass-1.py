def search(pat, txt):
    m = len(pat)
    n = len(txt)
    for i in range(n-m+1):
        if pat == txt[i:i+m]:
            return i
    return -1
