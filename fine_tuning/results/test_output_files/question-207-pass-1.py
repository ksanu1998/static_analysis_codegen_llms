def findNumber(n):
    for (i = 1; i <= n; i++)
        if (i * i == n)
            print(i, n / i)
    findNumber(n - 1)


if __name__ == "__main__":
    n = 4
    findNumber(n)
