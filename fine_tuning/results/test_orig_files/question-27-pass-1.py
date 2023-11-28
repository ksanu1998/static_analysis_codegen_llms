def calculate(p, q):

def calculate(p, q):
    # Calculate the modular inverse of q modulo 998244353
    # using the extended Euclidean algorithm
    a, b = q, p
    x, y = 0, 1
    while b!= 0:
        a, b = b, a % b
        x, y = y, x - y * (a // b)
    modular_inverse = x % p
    return modular_inverse
