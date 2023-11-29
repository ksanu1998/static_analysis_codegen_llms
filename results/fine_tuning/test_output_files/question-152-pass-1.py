def calculate(n, k, m, power):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (power[n]!= -1):
        return power[n]
    power[n] = (calculate(n - 1, k, m, power) +
                calculate(n - 1, k - 1, m, power))
    if (m == 1):
        power[n] = (power[n] + calculate(n - 1, k, m, power))
    return power[n]


if __name__ == "__main__":
    n = 3
    k = 2
    m = 1
    power = [-1] * (n + 1)
    print(calculate(n, k, m, power))
