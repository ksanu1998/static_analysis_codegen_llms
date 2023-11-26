'


def lps(str):
    n = len(str)
    lps = [0] * n
    i = 1
    while i < n:
        if str[i] == str[0]:
            lps[i] = 1
        else:
            lps[i] = max(lps[i-1], 1)
        i += 1
    return lps
