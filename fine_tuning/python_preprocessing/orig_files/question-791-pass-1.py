def calculateSpan(A, n, ans):
    ans[0] = 1
    for i in range(1, n):
        counter = 1
        while ((i - counter) >= 0 and A[i] >= A[i - counter]):
            counter += ans[i - counter]
        ans[i] = counter


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [0] * (n)
calculateSpan(price, n, S)
printArray(S, n)
