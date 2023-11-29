def countOfGreaterElements(arr, n):
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        cnt[i] = cnt[i - 1] + 1
    for i in range(1, n + 1):
        cnt[i] += cnt[i]
    for i in range(1, n + 1):
        print(cnt[i] - 1, end=" ")


arr = [1, 2, 3, 4, 5]
n = len(arr)
countOfGreaterElements(arr, n)
