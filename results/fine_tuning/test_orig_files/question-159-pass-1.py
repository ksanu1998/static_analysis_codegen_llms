from math import sqrt
MAX = 1000000
prime = [True] * (MAX + 1)



def SieveOfEratosthenes():
    for i in range(2, int(sqrt(MAX)) + 1):
        if prime[i]:
            for j in range(i * i, MAX + 1, i):
                prime[j] = False
    return [i for i in range(2, MAX + 1) if prime[i]]
