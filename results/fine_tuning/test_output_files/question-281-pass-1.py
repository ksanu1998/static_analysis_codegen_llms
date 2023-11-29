import math as mt
MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfErastosthenes():
    for i in range(2, int(mt.sqrt(MAX)) + 1):
        if (prime[i]):
            for j in range(i * i, MAX + 1, i):
                prime[j] = False


SieveOfErastosthenes()
n = 5
print(product(n))
