def find_and(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result &= arr[i]
    return result
