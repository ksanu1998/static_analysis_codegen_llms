def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest!= i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
