MOD = 1000000007



def power(x, y, p=MOD):
    if y == 0:
        return 1
    t = power(x, y // 2, p)
    t = (t * t) % p
    if y % 2 == 1:
        t = (t * x) % p
    return t
