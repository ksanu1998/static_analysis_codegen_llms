def checkIfPossibleRec(x, a, b, isPossible, n):
    if n == 0:
        return True
    if x == len(a) or x == len(b):
        return False
    if checkIfPossibleRec(x + 1, a, b, isPossible, n - a[x]):
        return True
    if checkIfPossibleRec(x + 1, a, b, isPossible, n - b[x]):
        return True
    return False