spf = [0 for i in range(10001)]



def spf_array(spf):
    for i in range(1, 10001):
        if spf[i] == 0:
            spf[i] = i
        for j in range(i, 10001, i):
            spf[j] = min(spf[j], i)
    return spf
