def calculate(p, q):
    # Calculate the modular inverse of q modulo 998244353
    # Using the extended Euclidean algorithm
    d, x, y = ext_gcd(q, 998244353)
    if d!= 1:
        raise ValueError("q and 998244353 are not relatively prime")
    return x % 998244353

def ext_gcd(a, b):
    # Extended Euclidean algorithm
    # Returns gcd(a, b), x, and y such that a*x + b*y = gcd(a, b)
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
