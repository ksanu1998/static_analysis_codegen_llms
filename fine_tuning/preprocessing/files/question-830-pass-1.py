def buildMaxHeap(arr, n):
    # Build the max heap by recursively calling heapify on the parent node
    # until the root node is reached.
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    return arr

def heapify(arr, n, i):
    # Find the largest child node of the current node and swap it with the
    # current node if necessary.
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest!= i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the larger child node.
        heapify(arr, n, largest)
