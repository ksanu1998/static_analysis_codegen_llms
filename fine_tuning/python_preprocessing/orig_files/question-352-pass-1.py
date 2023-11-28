def MinimumCost(a, n, x):
    for i in range(1, n, 1):
        a[i] = min(a[i], 2 * a[i - 1])
    ind = 0
    sum = 0
    while (x):
        if (x & 1):
            sum += a[ind]
        ind += 1
        x = x >> 1
    return sum


if __name__ == '__main__':
    a = [20, 50, 60, 90]
    x = 7
    n = len(a)
    print(MinimumCost(a, n, x))
