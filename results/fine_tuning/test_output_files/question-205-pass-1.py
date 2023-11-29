def NumbersofWays(n):
    if (n == 1):
        print(1)
        return
    print(NumbersofWays(n - 1))
    print(NumbersofWays(n - 1))


if __name__ == "__main__":
    n = 4
    NumbersofWays(n)
