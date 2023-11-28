arr = [True] * (1001)


def simpleSieve(n):
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    return [i for i in range(2, n + 1) if arr[i]]
