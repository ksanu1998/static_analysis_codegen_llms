def rec(a, i):
    if (i == 0):
        a .pop()
        print("".join(a))
        return
    if (a[i] == 'x'):
    j = i
    while (a[j] != '\0' and a[j + 1] != '\0'):
        (a[j], a[j + 1]) = (a[j + 1], a[j])
        j += 1
    rec(a, i - 1)


if __name__ == "__main__":
    a = ['g', 'e', 'e', 'k', 'x', 's', 'x', 'x', 'k', 's', '\0']
    n = 10
    rec(a, n - 1)
