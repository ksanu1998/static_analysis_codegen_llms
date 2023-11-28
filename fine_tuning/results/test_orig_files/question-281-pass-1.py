import math as mt
MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfErastosthenes():

for i in range(2, int(mt.sqrt(MAX)) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False


def get_product_of_first_n_prime_numbers(n):
    prime_numbers = []
    for i in range(2, MAX + 1):
        if prime[i]:
            prime_numbers.append(i)
            if len(prime_numbers) == n:
                break
    return int(mt.prod(prime_numbers))
