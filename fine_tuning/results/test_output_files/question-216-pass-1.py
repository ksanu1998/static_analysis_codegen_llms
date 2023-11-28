def checkSpecialPrime(sieve, num):
    if (sieve[num] == 1)
        return 1
    return 0


if __name__ == "__main__":
    sieve = [1] * 100
    for i in range(2, 100):
        if (sieve[i] == 1)
            continue
        for j in range(i * i, 100, i):
            sieve[j] = 1
    num = 10
    print(checkSpecialPrime(sieve, num))
