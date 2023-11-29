fact = [0] * 21


def preCompute():
    fact[0] = 1
    for i in range(1, 21):
        fact[i] = (i * fact[i - 1])


def nextFactorial(n):
    preCompute()
    if (n == 0):
        return 1
    return (fact[n] + 1)


if __name__ == "__main__":
    n = 10
    print(nextFactorial(n))
