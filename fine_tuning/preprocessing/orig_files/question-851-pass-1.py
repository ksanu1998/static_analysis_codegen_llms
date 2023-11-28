N = 1000000
phi = [0 for i in range(N + 5)]


def computeTotient():
    for i in range(1, N + 1):
        phi[i] = i
    for p in range(2, N + 1):
        if (phi[p] == p):
            phi[p] = p - 1
            for i in range(2 * p, N + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)


def power(x, y, p):
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        x = (x * x) % p
    return res


def calculate(x, k, mod):
    arr = [0 for i in range(N)]
    count = 0
    while (mod > 1):
        arr[count] = mod
        count += 1
        mod = phi[mod]
    result = 1
    loop = count + 1
    arr[count] = 1
    for i in range(min(k, loop), -1, -1):
        result = power(x, result, arr[i])
    return result


computeTotient()
x = 3
k = 2
m = 3
print(calculate(x, k, m))
