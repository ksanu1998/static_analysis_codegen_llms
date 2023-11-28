def isHeap(arr, n):
    for i in range(n):
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True
