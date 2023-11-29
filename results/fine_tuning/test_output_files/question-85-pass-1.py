def printPair(n):
    for (i in range(1, n + 1))
        for (j in range(1, n + 1))
            if (gcd(i, j) == n and lcm(i, j) == n):
                print(i, j)


if __name__ == "__main__":
    n = 12
    printPair(n)
