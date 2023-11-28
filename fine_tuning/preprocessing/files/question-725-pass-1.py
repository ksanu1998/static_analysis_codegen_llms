def nCk(n, k):import itertools

def nCk(n, k):
    return len(list(itertools.combinations(range(n), k)))
