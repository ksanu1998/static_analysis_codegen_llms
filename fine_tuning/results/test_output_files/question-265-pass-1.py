def checkIfPossibleRec(x, a, b, isPossible, n):
    if (n == 0):
        isPossible[0] = 1
        return
    if (a >= n):
        isPossible[0] = 0
        return
    if (b >= n):
        isPossible[0] = 1
        return
    checkIfPossibleRec(x, a + 1, b, isPossible, n - a)
    checkIfPossibleRec(x, a, b + 1, isPossible, n - b)


if __name__ == "__main__":
    n = 3
    isPossible = [0]
    checkIfPossibleRec(n, 1, 1, isPossible, n)
    if (isPossible[0] == 1):
        print("Yes")
    else:
        print("No")
