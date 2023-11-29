def findTwoThreePrime(l, r):
    count = 0
    for i in range(l, r+1):
        if i % 2 == 0 or i % 3 == 0:
            count += 1
    return count