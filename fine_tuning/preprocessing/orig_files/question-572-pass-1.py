def MaxFreq(s):
    n = len(s)
    m = dict()
    for i in range(n):
        string = ''
        for j in range(i, n):
            string += s[j]
            if string in m .keys():
                m[string] += 1
            else:
                m[string] = 1
    maxi = 0
    maxi_str = ''
    for i in m:
        if m[i] > maxi:
            maxi = m[i]
            maxi_str = i
        elif m[i] == maxi:
            ss = i
            if len(ss) > len(maxi_str):
                maxi_str = ss
    return maxi_str


string = "ababecdecd"
print(MaxFreq(string))
