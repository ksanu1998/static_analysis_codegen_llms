def repeatedSum(n):
    if (n == 0):
        return 0
    return 9 if (n % 9 == 0)else (n % 9)


def repeatedProduct(n):
    prod = 1
    while (n > 0 or prod > 9):
        if (n == 0):
            n = prod
            prod = 1
        prod *= n % 10
        n //= 10
    return prod


def maxSumProduct(N):
    if (N < 10):
        return N
    return max(repeatedSum(N), repeatedProduct(N))


if __name__ == "__main__":
    n = 631
    print(maxSumProduct(n))
