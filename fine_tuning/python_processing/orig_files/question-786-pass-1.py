def sumOfDigits(N):
    sum = 0
    while (N != 0):
        sum += N % 10
        N //= 10
    return sum


def elementsHavingDigitSumK(arr, N, K):
    count = 0
    for i in range(N):
        if (sumOfDigits(arr[i]) == K):
            count += 1
    print(count)


arr = [23, 54, 87, 29, 92, 62]
K = 11
N = len(arr)
elementsHavingDigitSumK(arr, N, K)
