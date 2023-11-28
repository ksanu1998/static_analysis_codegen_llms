N = 1000000007


def exponentiation(bas, exp):
    if exp == 0:
        return 1
    else:
        bas *= bas
        exp >>= 1
        return exponentiation(bas, exp) if exp else bas
