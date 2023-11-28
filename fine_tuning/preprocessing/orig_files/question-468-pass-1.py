def search(pat, txt):
    M = len(pat)
    N = len(txt)
    i = 0
    while i <= N - M:
        for j in xrange(M):
            if txt[i + j] != pat[j]:
                break
            j += 1
            print "Pattern found at index " + str(i)
            i = i + M
        elif j == 0:
            i = i + 1
        else:
            i = i + j


txt = "ABCEABCDABCEABCD"
pat = "ABCD"
search(pat, txt)
