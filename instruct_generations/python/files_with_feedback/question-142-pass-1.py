MOD = 2019



def min_modulo(l, r):
    if l % MOD < r % MOD:
        return l
    else:
        return r
