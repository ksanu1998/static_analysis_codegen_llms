def count_pairs(x):
    n = 1 << 10
    cnt = [0] * n
    cnt[0] = 1
    for i in range(1, n):
        cnt[i] = cnt[i & (i - 1)] + 1
    res = 0
    for i in range(1, n):
        for j in range(i, n):
            if (cnt[i] <= x and cnt[j] <= x and (i | j) <= x):
                res += 1
    print(res)
