def checkSpecialPrime(sieve, num):
    for i in range(num, 2 * num + 1):
        if i not in sieve:
            return i
    return -1