import math as mt


def candies(n, k):
    if (n < k):
        print("-1")
        return
    n = n - k
    a = 1
    b = 1
    c = 1
    d = 1
    while (n > 0):
        if (n >= a):
            a = a + 1
            n = n - a
        else:
            if (n >= b):
                b = b + 1
                n = n - b
            else:
                if (n >= c):
                    c = c + 1
                    n = n - c
                else:
                    d = d + 1
                    n = n - d
    print(a, b, c, d)


if __name__ == "__main__":
    n = 10
    k = 4
    candies(n, k)
