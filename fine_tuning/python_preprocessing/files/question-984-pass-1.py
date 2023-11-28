def computeTotient(n):
    totient = [0] * (n + 1)
    for i in range(2, n + 1):
        if totient[i] == 0:
            totient[i] = i - 1
        for j in range(i * i, n + 1, i):
            totient[j] -= totient[j] // i
    return totient
