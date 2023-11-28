from array import *
from math import *


def countOddIntegers(arr, N):
    Fact = [0] * N
    Fact[0] = 1
    for i in range(1, N):
        Fact[i] = i * Fact[i - 1]
    freq = [0] * 10
    for i in range(len(freq)):
        freq[i] = 0
    for i in range(N):
        freq[arr[i]] = freq[arr[i]] + 1
    ans = 0
    for i in range(1, 10, 2):
        if (freq[i] == 0):
            continue
        freq[i] = freq[i] - 1
        for j in range(1, 10, 1):
            cur_ans = 0
            if (freq[j] == 0):
                continue
            freq[j] = freq[j] - 1
            cur_ans = Fact[N - 2]
            for k in range(10):
                cur_ans = cur_ans / Fact[freq[k]]
            ans += cur_ans
            freq[j] = freq[j] + 1
        freq[i] = freq[i] + 1
    return ceil(ans)


if __name__ == "__main__":
    A = [2, 3, 4, 1, 2, 3]
    N = len(A)
    print(countOddIntegers(A, N))
