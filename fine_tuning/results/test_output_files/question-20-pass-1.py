def modexp(x, n, m):
    if (n == 0):
        return 1
    if (n == 1):
        return x
    if (n & 1):
        return (((x * modexp(x, n - 1, m)) % m) * (x % m)) % m
    y = modexp(x, n / 2, m)
    y = (y * y) % m
    if (n & 1):
        return (((x * y) % m) * (x % m)) % m
    return (y * (x % m)) % m


N = 1000000007


def countDistinct(N):
    ans = modexp(2, N, N)
    print(ans)


if __name__ == "__main__":
    countDistinct(N)
