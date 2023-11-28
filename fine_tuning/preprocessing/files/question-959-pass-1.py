MAX = 100001
phi = [0] * MAX
result = [0] * MAX


def computeTotient(n):
    if n == 1:
        return 1
    else:
        return n - sum(computeTotient(i) for i in range(2, int(n ** 0.5) + 1) if n % i == 0)
