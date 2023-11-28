MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfEratosthenes():

for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False


def get_xor_of_first_n_prime_numbers(n):
    prime_numbers = []
    for i in range(2, MAX + 1):
        if prime[i]:
            prime_numbers.append(i)
            if len(prime_numbers) == n:
                break
    return sum(prime_numbers)


print(get_xor_of_first_n_prime_numbers(10))
