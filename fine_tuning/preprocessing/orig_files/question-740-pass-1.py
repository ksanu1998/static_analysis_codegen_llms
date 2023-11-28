def maxRightmostElement(N, k, arr):
    ans = arr[N - 1]
    i = N - 2
    while (i >= 0):
        d = min(arr[i] // 2, k // (N - 1 - i))
        k -= d * (N - 1 - i)
        ans += d * 2
        i -= 1
    print(ans, end=" ")


if __name__ == '__main__':
    N = 4
    k = 5
    arr = [3, 8, 1, 4]
    maxRightmostElement(N, k, arr)
