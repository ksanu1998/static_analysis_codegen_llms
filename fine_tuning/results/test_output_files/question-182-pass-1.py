def solve(a, n):
    a.sort()
    for i in range(n - 1, -1, -1):
        if (a[i] == 1):
            a[i] = 0
        else:
            a[i] = 1
    print(a)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(a)
    solve(a, n)
