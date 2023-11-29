sieve = [1] * (1000000 + 1)


def sieveOfPrimes():
    for i in range(2, 1000000 + 1):
        if (sieve[i] == 1):
            continue
        for j in range(i * i, 1000000 + 1, i):
            sieve[j] = 1


if __name__ == "__main__":
    sieveOfPrimes()
    print(sieve[1000000])
