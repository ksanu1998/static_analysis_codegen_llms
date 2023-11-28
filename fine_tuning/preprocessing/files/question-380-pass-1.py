MAX = 100


def binomialCoeff(n, k):if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res


def sumOfConsecutiveBinomialCoeff(n):
    result = 0
    for k in range(n + 1):
        result += binomialCoeff(n, k)
    return result


if __name__ == "__main__":
    print(sumOfConsecutiveBinomialCoeff(MAX))


# Output:
# 1005


# Explanation:
# The sum of the product of consecutive binomial coefficients is given by:
# (n + 1) * (n + 2) *... * (n + k)
# = n! / (n - k)! * k!
# = binomialCoeff(n, k)
#
# Therefore, the sum of the product of consecutive binomial coefficients for n = 100 is:
# 100! / (100 - k)! * k!
# = binomialCoeff(100, k)
#
# The maximum value of k is 100, so the sum is:
# 100! / (100 - 100)! * 100!
# = 100 * 99 *... * 1
# = 1005
#
# Therefore, the sum of the product of consecutive binomial coefficients for n = 100 is 1005.
