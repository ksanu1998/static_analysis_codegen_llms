import math


def isPrime(n):
    if (n == 1) or (n == 0):
        return 0
    for (i in range(2, int(math.sqrt(n)) + 1)):
        if (n % i == 0):
            return 0
    return 1


if __name__ == "__main__":
    n = 2
    if (isPrime(n)):
        print("Yes")
    else:
        print("No")
