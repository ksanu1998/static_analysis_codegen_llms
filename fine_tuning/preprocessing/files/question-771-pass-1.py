def makeSumX(arr, X, S, i):
    if i == len(arr):
        return False
    if S + arr[i] == X:
        return True
    if makeSumX(arr, X, S + arr[i], i + 1):
        return True
    return makeSumX(arr, X, S, i + 1)
