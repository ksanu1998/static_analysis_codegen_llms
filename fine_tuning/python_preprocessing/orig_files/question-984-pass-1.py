def computeTotient(n):
    phi = []
    for i in range(n + 2):
        phi .append(0)
    for i in range(1, n + 1):
    for p in range(2, n + 1):
        if (phi[p] == p):
            phi[p] = p - 1
            for i in range(2 * p, n + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)
    for i in range(1, n + 1):
        print("Totient of ", i, " is ", phi[i])


n = 12
computeTotient(n)
