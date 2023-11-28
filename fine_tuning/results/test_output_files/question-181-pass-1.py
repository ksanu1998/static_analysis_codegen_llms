def gcd(a, b):
    if (a == 0):
        return b
    c = a
    a = b
    b = c
    c = a % b
    if (c == 0):
        return b
    c = b
    b = a
    a = c
    c = b % a
    if (c == 0):
        return a
    return 0


def countQuadruplets(arr, n, k):
    res = 0
    for (i, j) in zip(range(n - 1), range(1, n)):
        for (l, r) in zip(range(i + 1, j), range(j + 1, n)):
            if (gcd(arr[i], arr[j]) == k):
                res += 1
    print(res)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
k = 2
countQuadruplets(arr, n, k)
k = 3
countQuadruplets(arr, n, k)
k = 4
countQuadruplets(arr, n, k)
k = 5
countQuadruplets(arr, n, k)
k = 6
countQuadruplets(arr, n, k)
k = 7
countQuadruplets(arr, n, k)
k = 8
countQuadruplets(arr, n, k)
k = 9
countQuadruplets(arr, n, k)
k = 10
countQuadruplets(arr, n, k)
k = 11
countQuadruplets(arr, n, k)
k = 12
countQuadru
