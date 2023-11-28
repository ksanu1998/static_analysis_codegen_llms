MAX = 100001
phi = [0] * MAX
result = [0] * MAX


def computeTotient():
    phi[1] = 1
    for i in range(2, MAX):
        if not phi[i]:
            phi[i] = i - 1
            for j in range(i << 1, MAX, i):
                if not phi[j]:
                    phi[j] = j
                phi[j] = ((phi[j] // i) * (i - 1))


def sumOfGcdPairs():
    computeTotient()
    for i in range(MAX):
        for j in range(2, MAX):
            if i * j >= MAX:
                break
            result[i * j] += i * phi[j]
    for i in range(2, MAX):
        result[i] += result[i - 1]


sumOfGcdPairs()
N = 4
print("Summation of", N, "=", result[N])
N = 12
print("Summation of", N, "=", result[N])
N = 5000
print("Summation of", N, "=", result[N])
