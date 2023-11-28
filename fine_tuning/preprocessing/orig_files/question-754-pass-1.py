def tripletAndSum(arr, n):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n, 1):
            for k in range(j + 1, n, 1):
                ans += arr[i] & arr[j] & arr[k]
    print(ans)


if __name__ == '__main__':
    arr = [3, 5, 4, 7]
    N = len(arr)
    tripletAndSum(arr, N)
