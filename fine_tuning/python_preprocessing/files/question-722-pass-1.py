def isValid(arr, i, j, m, c):
    if i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0]) and arr[i][j] == m:
        return True
    return False
