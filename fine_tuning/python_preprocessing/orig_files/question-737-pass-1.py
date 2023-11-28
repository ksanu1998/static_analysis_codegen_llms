import math


def countDivisors(n):
    divisors = 0
    for i in range(1, math .ceil(math .sqrt(n)) + 1):
        if n % i == 0:
            divisors = divisors + 1
        if (i - (n / i) == 1):
            i = i - 1
    for i in range(math .ceil(math .sqrt(n)) + 1, 1, -1):
        if (n % i == 0):
            divisors = divisors + 1
    return divisors


def possibleTriplets(N):
    count = 0
    for i in range(1, N):
        count = count + countDivisors(N - i)
    return count


if __name__ == "__main__":
    N = 10
    print(possibleTriplets(N))
