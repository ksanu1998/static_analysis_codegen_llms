def checkIsAP(arr, n):

def checkIsAP(arr, n):
    if n <= 1:
        return False
    for i in range(n-1):
        if arr[i+1] - arr[i]!= arr[1] - arr[0]:
            return False
    return True
