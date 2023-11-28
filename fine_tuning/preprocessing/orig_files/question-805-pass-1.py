def printMaxOfMin(arr, n):
    s = []
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
    for i in range(n):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s .pop()
        if (len(s) != 0):
            left[i] = s[-1]
        s .append(i)
    while (len(s) != 0):
        s .pop()
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s .pop()
        if (len(s) != 0):
            right[i] = s[-1]
        s .append(i)
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = 0
    for i in range(n):
        Len = right[i] - left[i] - 1
        ans[Len] = max(ans[Len], arr[i])
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    for i in range(1, n + 1):
        print(ans[i], end=" ")


if __name__ == '__main__':
    arr = [10, 20, 30, 50, 10, 70, 30]
    n = len(arr)
    printMaxOfMin(arr, n)
