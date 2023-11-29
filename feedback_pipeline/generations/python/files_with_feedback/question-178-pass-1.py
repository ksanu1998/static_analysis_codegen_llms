def getfactor(n, p):
    if n % p == 0:
        return p
    else:
        return getfactor(n // p, p)
