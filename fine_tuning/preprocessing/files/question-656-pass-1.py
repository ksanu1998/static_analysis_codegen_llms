MAX = 100
store = [0 for i in range(MAX)]
n = 0
graph = [[0 for j in range(MAX)]for i in range(MAX)]
d = [0 for i in range(MAX)]
ans = 0


def SieveOfEratosthenes(prime, p_size):
    for i in range(2, p_size):
        if prime[i] == 1:
            for j in range(i*i, p_size, i):
                prime[j] = 0
