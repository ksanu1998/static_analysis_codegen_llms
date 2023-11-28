def isHeap(arr, i, n):
    if i >= n // 2:
        return True
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[i]:
        return False
    if right < n and arr[right] > arr[i]:
        return False
    return isHeap(arr, left, n) and isHeap(arr, right, n)
