def arrange(s):
    cc = 0
    for i in range(len(s)):
        if (s[i] == "1"):
            cc += 1
    a = [0] * (len(s) + 1)
    qq = [(2, 3), (5, 5)]
    n = len(qq)
    for i in range(n):
        l, r = qq[i][0], qq[i][1]
        l -= 1
        r -= 1
        a[l] += 1
        a[r + 1] -= 1
    for i in range(1, len(a)):
        a[i] = a[i] + a[i - 1]
    zz = [0] * len(s)
    for i in range(len(a) - 1):
        if (a[i] > 0):
            if (cc > 0):
                zz[i] = 1
                cc -= 1
            else:
                break
        if (cc == 0):
            break
    if (cc > 0):
        for i in range(len(s)):
            if (zz[i] == 0):
                zz[i] = 1
                cc -= 1
            if (cc == 0):
                break
    print(*zz, sep="")


str = "11100"
arrange(str)
