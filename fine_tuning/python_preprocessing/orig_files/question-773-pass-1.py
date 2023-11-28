import math


def cntPairs(arr, N):
    res = 0
    bit = [0] * 32
    for i in range(N):
        pos = (int)(math .log2(arr[i]))
        bit[pos] += 1
    for i in range(32):
        res += (bit[i] * (bit[i] - 1)) // 2
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    N = len(arr)
    print(cntPairs(arr, N))
