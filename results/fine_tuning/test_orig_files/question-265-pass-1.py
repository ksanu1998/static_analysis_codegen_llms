def checkIfPossibleRec(x, a, b, isPossible, n):

def checkIfPossibleRec(x, a, b, isPossible, n):
    if n == 0:
        return True
    if x == 0:
        return False
    if isPossible[x]:
        return checkIfPossibleRec(x - a, a, b, isPossible, n - 1) or checkIfPossibleRec(x - b, a, b, isPossible, n - 1)
    else:
        return checkIfPossibleRec(x - a, a, b, isPossible, n - 1)
