def findDivisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if (i % 2 == 0):
            divisors = divisors + 1
        for j in range(1, i):
            if (i % j == 0):
                divisors = divisors + 1
    print(divisors)


if __name__ == "__main__":
    findDivisors(10)
