def expectedValue(P, a, b, N):
    expValue = P + (N * 0.5 * (a + b))
    print(int(expValue))


if __name__ == '__main__':
    P = 3000
    a = 20
    b = 10
    N = 30
    expectedValue(P, a, b, N)
