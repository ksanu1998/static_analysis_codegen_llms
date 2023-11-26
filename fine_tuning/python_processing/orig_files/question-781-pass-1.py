def maxModProdSubarr(arr, n, M):
    ans = 0
    length = n
    for i in range(n):
        product = 1
        for j in range(i, n, 1):
            product = (product * arr[i]) % M
            if (product > ans):
                ans = product
                if (length > j - i + 1):
                    length = j - i + 1
    print("Maximum subarray product is", ans)
    print("Minimum length of the maximum product subarray is", length)


if __name__ == '__main__':
    arr = [2, 3, 4, 2]
    N = len(arr)
    M = 5
    maxModProdSubarr(arr, N, M)
