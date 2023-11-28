MAX = 100
store = [0 for i in range(MAX)]
n = 0
graph = [[0 for j in range(MAX)]for i in range(MAX)]
d = [0 for i in range(MAX)]
ans = 0


def SieveOfEratosthenes(prime, p_size):
    prime[0] = False
    prime[1] = False
    p = 2
    while (p * p <= p_size):
        if (prime[p]):
            for i in range(p * 2, p_size + 1, p):
                prime[i] = False
        p += 1


def is_clique(b):
    for i in range(1, b):
        for j in range(i + 1, b):
            if (graph[store[i]][store[j]] == 0):
                return False
    return True


def primeCliques(i, l, prime):
    global ans
    for j in range(i + 1, n + 1):
        store[l] = j
        if (is_clique(l + 1)):
            if (prime[l]):
                ans += 1
            primeCliques(j, l + 1, prime)


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 1], [4, 3], [4, 5], [5, 3]]
    size = len(edges)
    n = 5
    prime = [True for i in range(n + 2)]
    SieveOfEratosthenes(prime, n + 1)
    for i in range(size):
        graph[edges[i][0]][edges[i][1]] = 1
        graph[edges[i][1]][edges[i][0]] = 1
        d[edges[i][0]] += 1
        d[edges[i][1]] += 1
    ans = 0
    primeCliques(0, 1, prime)
    print(ans)
