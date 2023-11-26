def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        (arr[i], arr[smallest]) = (arr[smallest], arr[i])
        heapify(arr, n, smallest)


def heapSort(arr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [4, 6, 3, 2, 9]
    n = len(arr)
    heapSort(arr, n)
    print("Sorted array is ")
    printArray(arr, n)
