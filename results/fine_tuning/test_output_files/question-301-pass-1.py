from math import sqrt
MAX = 10000
prefix = [0 for i in range(MAX + 1)]


def buildPrefix():
    for i in range(2, sqrt(MAX) + 1):
        if (prefix[i] == 0):
            for j in range(i * i, MAX + 1, i):
                prefix[j] = 1


def sumOfPrimes(n):
    buildPrefix()
    sum = 0
    for i in range(2, n + 1):
        if (prefix[i] == 0):
            sum += i
    print(sum)


if __name__ == "__main__":
    sumOfPrimes(10000)
