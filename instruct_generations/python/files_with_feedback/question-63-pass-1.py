def lowerBound(array, length, value):
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1
    return left
