def checkDigits(n):
    while (n):
        dig = n % 10
        if (dig != 2 and dig != 3 and dig != 5 and dig != 7):
            return 0
        n = n / 10
    return 1


def prime(n):
    if (n == 1):
        return 0
    i = 2
    while i * i <= n:
        if (n % i == 0):
            return 0
        i = i + 1
    return 1


def isFullPrime(n):
    return (checkDigits(n) and prime(n))


n = 53
if (isFullPrime(n)):
    print("Yes")
else:
    print("No")
