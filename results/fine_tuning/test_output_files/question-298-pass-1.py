def numberOfSolutions(n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    x = (n - 1) / 2
    if (x == 0):
        return 1
    if (x < 0):
        return 0
    return (numberOfSolutions(x) * (x + 1))


if __name__ == "__main__":
    n = 10
    print(numberOfSolutions(n))
