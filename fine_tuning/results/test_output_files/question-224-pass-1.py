from math import sqrt


def smallestDivisor(n):
    sq = int(sqrt(n))
    for i in range(1, sq + 1):
        if (n % i == 0):
            print(i)


if __name__ == "__main__":
    smallestDivisor(12)
