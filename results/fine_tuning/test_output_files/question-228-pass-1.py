import math


def max_gcd(n, p):
    gcd = 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            gcd = math.gcd(i, p)
            if (gcd > 1):
                break
    print(gcd)


if __name__ == "__main__":
    n = 12
    p = 15
    max_gcd(n, p)
