prime = [True] * 100001


def SieveOfEratosthenes(n):
    global prime
    for p in range(2, n + 1):
        if p * p > n:
            break
        if (prime[p]):
            for i in range(p * p, n + 1, p):
                prime[i] = False


def NumberofSets(N):
    SieveOfEratosthenes(N)
    if (N == 2):
        print(1)
    elif (N == 3):
        print(2)
    else:
        ans = 1
        for i in range(N // 2, N + 1):
            if (prime[i]):
                ans += 1
        print(ans)


if __name__ == '__main__':
    N = 9
    NumberofSets(N)
