def makeAP(arr, n):

def makeAP(arr, n):
    for i in range(1, n):
        arr[i] = arr[i-1] + (i * 2)
    return arr
