def cost(st):
    l = len(st)
    res = 0
    j = l - 1
    i = 0
    while (i < j):
        if (st[i] != st[j]):
            res += (min(ord(st[i]), ord(st[j])) - ord('a') + 1)
        i = i + 1
        j = j - 1
    return res


st = "abcdef"
print(cost(st))
