def convert(n, a, b):
    l = [0] * n
    for i in range(n):
        if (a[i] != b[i]):
            l[i] = 1
    cc = 0
    vl = 0
    for i in range(n):
        if (l[i] == 0):
            if (vl != 0):
                cc += 1
            vl = 0
        else:
            vl += 1
    if (vl != 0):
        cc += 1
    print(cc)


a = "101010"
b = "110011"
n = len(a)
convert(n, a, b)
