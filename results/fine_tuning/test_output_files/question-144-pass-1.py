def countPairs(arr, n):
    freq = [0] * (n + 1)
    for i in range(n):
        freq[arr[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        if (freq[i] > 1):
            ans += (freq[i] * (freq[i] - 1)) / 2
    print(ans)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
countPairs(arr, n)
