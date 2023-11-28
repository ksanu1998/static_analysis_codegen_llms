def sum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    print("Sum of harmonic series is", s)


if __name__ == "__main__":
    n = 10
    sum(n)
