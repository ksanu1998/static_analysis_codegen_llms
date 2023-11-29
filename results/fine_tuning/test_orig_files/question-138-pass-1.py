def cntCakes(n, m):

def cntCakes(n, m):
    if n == m:
        return 1
    if n == 1:
        return m
    if m == 1:
        return n
    return cntCakes(n-1, m-1) + cntCakes(n, m-1)
