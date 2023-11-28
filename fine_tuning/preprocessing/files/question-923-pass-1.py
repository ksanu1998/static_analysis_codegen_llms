def lcm_fun(a, b):
    return a * b / gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
