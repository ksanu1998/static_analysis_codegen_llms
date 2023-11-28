def printCollatz(n):
    if n <= 0:
        return
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        printCollatz(n // 2)
    else:
        printCollatz(3 * n + 1)
