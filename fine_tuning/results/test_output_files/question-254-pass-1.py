import math


def findLargestDivisor(n):
    sq = int(math.sqrt(n))
    for i in range(1, sq + 1):
        if (n % i == 0):
            if (i * i == n):
                return i
    return -1


if __name__ == "__main__":
    n = 12
    print(findLargestDivisor(n))
