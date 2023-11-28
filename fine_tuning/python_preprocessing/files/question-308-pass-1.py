def printPair(g, l):
    for i in range(1, g):
        if (g % i == 0) and (l % i == 0):
            print(i)
