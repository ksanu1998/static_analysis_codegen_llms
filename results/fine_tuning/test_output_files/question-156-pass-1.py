MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfEratosthenes():
    for i in range(2, MAX + 1):
        if (prime[i]):
            for j in range(i * i, MAX + 1, i):
                prime[j] = False


SieveOfEratosthenes()
n = 10
ans = 0
for i in range(2, n + 1):
    if (prime[i]):
        ans = ans ^ i
print(ans)
