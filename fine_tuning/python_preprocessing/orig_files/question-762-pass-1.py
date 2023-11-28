def fact(N):
    if (N == 1 or N == 0):
        return 1
    return N * fact(N - 1)


def prefixFactorialArray(arr, N):
    for i in range(1, N):
        arr[i] += arr[i - 1]
    for i in range(N):
        arr[i] = fact(arr[i])
    for i in range(N):
        print(arr[i], end=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    N = len(arr)
    prefixFactorialArray(arr, N)
