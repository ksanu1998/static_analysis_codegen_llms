def CntDivbyX(arr, n, x):

def CntDivbyX(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] % x == 0:
            count += 1
    return count
