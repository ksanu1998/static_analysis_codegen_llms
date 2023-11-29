from math import sqrt
MAX = 1000000
prime = [True] * (MAX + 1)


def SieveOfEratosthenes():
    for (i = 2; i <= sqrt(MAX); i += 1)
        if (prime[i] == True):
            for (j = i * i; j <= MAX; j += i)
                prime[j] = False


SieveOfEratosthenes()


def generate(n):
    if (n == 1):
        print(1)
        return
    if (n == 2):
        print(2)
        return
    if (n == 3):
        print(3)
        return
    if (n == 4):
        print(2)
        print(2)
        return
    if (n == 5):
        print(5)
        print(5)
        return
    if (n == 6):
        print(2)
        print(3)
        print(3)
        return
    if (n == 7):
        print(7)
        print(7)
        return
    if (n == 8):
        print(2)
        print(2)
        print(2)
        print(2)
        return
    if (n == 9):
        print(3)
        print(3)
        print(3)
        print(3)
        return
    if (n == 10):
        print(2)
        print(5)
        print(5)
        print(5)
        return
    if (n == 11):
        print(11)
        print(11)
        return
    if (n == 12):
        print(2)
        print(2)
        print(2)
        print(2)
