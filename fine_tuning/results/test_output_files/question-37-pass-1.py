def isPrime(n):
    if (n == 1):
        return (False)
    for (i = 2; i <= n / 2; i++):
        if (n % i == 0):
            return (False)
    return (True)


def isMagnanimous(n):
    if (isPrime(n)):
        return (False)
    for (i = 2; i <= n / 2; i++):
        if (isPrime(i) and isPrime(n - i)):
            return (True)
    return (False)


if __name__ == "__main__":
    n = 10
    if (isMagnanimous(n)):
        print ("Yes")
    else:
        print ("No")
