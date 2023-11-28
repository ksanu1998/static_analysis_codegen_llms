def print_h_index(arr, N):
    arr.sort()
    for i in range(N - 1, -1, -1):
        if (arr[i] >= N - i):
            print(N - i)
            break
    if (N - i - 1 >= 0):
        print(N - i - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = len(arr)
print_h_index(arr, N)
