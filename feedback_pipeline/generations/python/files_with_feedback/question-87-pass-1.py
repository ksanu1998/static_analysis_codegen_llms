MAX = 100000
graph = [[]for i in range(MAX + 1)]
Prime = [True for i in range(MAX + 1)]
height = [0 for i in range(MAX + 1)]


def SieveOfEratosthenes():MAX = 100000
graph = [[] for i in range(MAX + 1)]
Prime = [True for i in range(MAX + 1)]
height = [0 for i in range(MAX + 1)]


def SieveOfEratosthenes():
    for p in range(2, int(MAX ** 0.5) + 1):
        if Prime[p]:
            for i in range(p * p, MAX + 1, p):
                Prime[i] = False
    return [p for p in range(2, MAX + 1) if Prime[p]]
