import math


def findMaxGCD(arr, n, k):
    high = max(arr)
    divisors = [0] * (high + 1)
    for i in range(n):
        for j in range(1, int(math .sqrt(arr[i])) + 1):
            if (arr[i] % j == 0):
                divisors[j] += 1
                if (j != arr[i] // j):
                    divisors[arr[i] // j] += 1
    for i in range(high, 0, -1):
        if (divisors[i] >= k):
            return i


if __name__ == "__main__":
    arr = [1, 2, 4, 8, 8, 12]
    k = 3
    n = len(arr)
    print(findMaxGCD(arr, n, k))
