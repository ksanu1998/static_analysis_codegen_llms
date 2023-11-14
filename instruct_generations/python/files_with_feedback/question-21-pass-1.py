spf = [0 for i in range(10001)]


def spf_array(spf):
    for i in range(2, len(spf)):
        if spf[i] == 0:
            spf[i] = i
        for j in range(i+1, len(spf)):
            if spf[j] == 0:
                spf[j] = spf[i]
            if spf[i] == spf[j]:
                spf[j] = i
    return spf
