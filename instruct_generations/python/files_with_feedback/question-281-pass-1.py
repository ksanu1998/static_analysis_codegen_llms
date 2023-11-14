import math as mt
MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfErastosthenes():import math as mt

MAX = 10000
prime = [True for i in range(MAX + 1)]

def SieveOfErastosthenes():
    for p in range(2, int(mt.sqrt(MAX)) + 1):
        if prime[p]:
            for i in range(p * p, MAX + 1, p):
                prime[i] = False
    return [p for p in range(2, MAX + 1) if prime[p]]
