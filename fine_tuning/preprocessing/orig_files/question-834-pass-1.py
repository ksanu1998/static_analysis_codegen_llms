def isHeap(arr, i, n):
    if i >= int((n - 2) / 2):
        return True
    if (arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2]
            and isHeap(arr, 2 * i + 1, n) and isHeap(arr, 2 * i + 2, n)):
        return True
    return False


if __name__ == '__main__':
    arr = [90, 15, 10, 7, 12, 2, 7, 3]
    n = len(arr) - 1
    if isHeap(arr, 0, n):
        print("Yes")
    else:
        print("No")
