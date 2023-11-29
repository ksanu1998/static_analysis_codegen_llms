def count(a, n):
    c = 0
    for (i = 0; i < n; i++)
        if (a[i] == 0)
            c++
    for (i = 0; i < n; i++)
        if (a[i] == 0)
            a[i] = 1
    for (i = 0; i < n; i++)
        if (a[i] == 0)
            c--
    print(c)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    n = 6
    count(a, n)
