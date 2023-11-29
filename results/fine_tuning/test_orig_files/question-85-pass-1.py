def printPair(n):

def printPair(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i % j == 0:
                print(i, j)
                break
