import math as m


def CountPairs(n):
    c = 0
    for i in range(1, int(m.sqrt(n)) + 1):
        if (n % i == 0):
            if (m.gcd(i, n / i) == 1):
                c += 1
    print(c)


if __name__ == "__main__":
    CountPairs(12)
