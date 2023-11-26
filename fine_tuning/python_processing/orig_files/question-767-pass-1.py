def check(arr, N):
    sum = 0
    for i in range(N):
        sum += arr[i]
    if (sum == 0):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    arr = [1, -1, 3, -2, -1]
    N = len(arr)
    check(arr, N)
