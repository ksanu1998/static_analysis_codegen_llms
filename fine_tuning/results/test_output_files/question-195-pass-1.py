max_Element = 100005
sum1 = [0 for i in range(max_Element)]
sum2 = [0 for i in range(max_Element)]
sum3 = [0 for i in range(max_Element)]


def precomputation(arr, n):
    for (i, j) in zip(range(1, n), range(n - 1, -1, -1)):
        sum1[i] = sum1[i - 1] + arr[i]
        sum2[j] = sum2[j + 1] + arr[j]

    for (i, j) in zip(range(1, n), range(n - 1, -1, -1)):
        sum3[i] = sum3[i - 1] + sum2[j]

    for (i, j) in zip(range(1, n), range(n - 1, -1, -1)):
        sum1[i] = sum1[i] - sum3[j]

    for (i, j) in zip(range(1, n), range(n - 1, -1, -1)):
        sum2[i] = sum2[i] - sum1[j]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
precomputation(arr, n)


def sumOfTriplet(arr, n):
    ans = 0
    for (i, j) in zip(range(1, n), range(n - 1, -1, -1)):
        ans = ans + (sum1[i] * sum2[j])
    print(ans)


sumOfTriplet(arr, n)
