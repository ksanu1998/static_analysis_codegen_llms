def reverse(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


def findPrimeAdam(L, R):
    a = [1]
    for i in range(2, R + 1):
        a.append(i)
    reverse(a)
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
    for i in range(1, len(a)):
        if (a[i] % 2 == 0):
            a[i] = 0
