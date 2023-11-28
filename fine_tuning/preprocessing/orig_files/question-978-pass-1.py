def gcd(a, b):
    if (b == 0):
        return a
    return (gcd(b, a % b))


def findSmallest(a, b):
    lcm = (a * b) / gcd(a, b)
    print("x =", lcm / a, "y=", lcm / b)


a = 25
b = 35
findSmallest(a, b)
