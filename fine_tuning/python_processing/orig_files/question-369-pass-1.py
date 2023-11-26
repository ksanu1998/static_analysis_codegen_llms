def maxCost(a, n, l, r):
    mx = 0
    for i in range(n):
        mx = max(mx, a[i])
    count = [0] * (mx + 1)
    for i in range(n):
        count[a[i]] += 1
    res = [0] * (mx + 1)
    res[0] = 0
    l = min(l, r)
    for num in range(1, mx + 1):
        k = max(num - l - 1, 0)
        res[num] = max(res[num - 1], num * count[num] + res[k])
    return res[mx]


if __name__ == "__main__":
    a = [2, 1, 2, 3, 2, 2, 1]
    l, r = 1, 1
    n = len(a)
    print(maxCost(a, n, l, r))
