def findTwoThreePrime(l, r):
    c = 0
    for i in range(l, r + 1):
        if (i % 2 == 0 or i % 3 == 0):
            c += 1
    print(c)


if __name__ == "__main__":
    findTwoThreePrime(1, 10)
