MOD = 1000000007



def power(x, y, p=MOD):
    if y == 0:
        return 1
    temp = power(x, y // 2, p)
    res = (temp * temp) % p
    if y % 2 == 1:
        res = (res * x) % p
    return res
