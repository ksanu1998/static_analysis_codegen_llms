def buildMaxHeap(arr, n):
    for i in range(n):
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i
            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j], arr[int((j - 1) / 2)]
                 ) = (arr[int((j - 1) / 2)], arr[j])
                j = int((j - 1) / 2)


def heapSort(arr, n):
    buildMaxHeap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        j, index = 0, 0
        while True:
            index = 2 * j + 1
            if (index < (i - 1) and arr[index] < arr[index + 1]):
                index += 1
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
            j = index
            if index >= i:
                break


if __name__ == '__main__':
    arr = [10, 20, 15, 17, 9, 21]
    n = len(arr)
    print("Given array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    heapSort(arr, n)
    print("Sorted array: ")
    for i in range(n):
        print(arr[i], end=" ")
