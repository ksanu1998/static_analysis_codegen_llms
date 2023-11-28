def isHeap(arr, n):
    for i in range(int((n - 2) / 2) + 1):
        if arr[2 * i + 1] > arr[i]:
            return False
        if (2 * i + 2 < n and arr[2 * i + 2] > arr[i]):
            return False
    return True


if __name__ == '__main__':
    arr = [90, 15, 10, 7, 12, 2, 7, 3]
    n = len(arr)
    if isHeap(arr, n):
        print("Yes")
    else:
        print("No")
