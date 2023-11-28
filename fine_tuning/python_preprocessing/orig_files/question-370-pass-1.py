def countPaths(m, n):
    if m == 1 or n == 1:
        return 1
    return (countPaths(m - 1, n) + countPaths(m, n - 1))


if __name__ == "__main__":
    n = 5
    m = 5
    print(countPaths(n, m))
