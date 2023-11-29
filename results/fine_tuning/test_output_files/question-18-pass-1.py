def solve(arr, n):
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                res += 1
    print(res)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
n = len(arr)
solve(arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
n = len(arr)
