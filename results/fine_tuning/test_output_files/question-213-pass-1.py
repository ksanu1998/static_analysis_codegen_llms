def maxLenSubArr(a, n):
    maxLen = 0
    for i in range(n):
        maxLen = max(maxLen,
                     a[i] +
                     maxLenSubArr(a, n - 1 - i))
    return maxLen


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(a)
    print(maxLenSubArr(a, n))
