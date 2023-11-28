import sys


def findMax(n, a, b, k, m):
    arr = [0] * n
    for i in range(m):
        lowerbound = a[i]
        upperbound = b[i]
        for j in range(lowerbound, upperbound + 1):
        arr[j] += k[i]
        res = -sys .maxsize - 1
        for i in range(n):
            res = max(res, arr[i])
            return res


if __name__ == "__main__":
    n = 5
    a = [0, 1, 2]
    b = [1, 4, 3]
    k = [100, 100, 100]
    m = len(a)
    print("Maximum value after 'm' operations is ", findMax(n, a, b, k, m))
