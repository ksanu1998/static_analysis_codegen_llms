def numbers(n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    c = numbers(n - 3)
    c += numbers(n - 4)
    return c


if __name__ == "__main__":
    n = 4
    print(numbers(n))
