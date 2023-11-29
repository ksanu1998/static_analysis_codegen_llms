def seriesSum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + (i * (n - i + 1))
    print(s)


if __name__ == "__main__":
    n = 5
    seriesSum(n)
