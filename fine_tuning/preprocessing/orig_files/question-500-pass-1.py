def permute(st, l, r, n):
    if (l == r):
        p = ''.join(st)
        j = int(p)
        if (j % n == 0):
            print(p)
        return
    for i in range(l, r):
        st[l], st[i] = st[i], st[l]
        permute(st, l + 1, r, n)
        st[l], st[i] = st[i], st[l]


if __name__ == "__main__":
    st = "125"
    n = 5
    length = len(st)
    if (length > 0):
    p = list(st)
    permute(p, 0, length, n)
