def factorial(f):
    if (f == 0):
        return 1
    if (f == 1):
        return 1
    res = 1
    for (i = 1; i <= f; i++)
        res = (res * i) % 1000000007;
    return res;


def count(n, m):
    res = 0
    for (i = 0; i <= n; i++)
        res = (res + (factorial(n - i) * factorial(m - 1) % 1000000007) % 1000000007) % 1000000007;
    return res;


if __name__ == "__main__":
    n = 3
    m = 2
    print(count(n, m))
