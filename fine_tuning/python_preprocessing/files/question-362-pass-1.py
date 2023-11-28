def nCr(n, r):import itertools

def nCr(n, r):
    return len(list(itertools.combinations(range(n), r)))
