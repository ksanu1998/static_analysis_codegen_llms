import sys


def maxProductSum(string, m):
    n = len(string)
    maxProd, maxSum = (-(sys .maxsize) - 1, -(sys .maxsize) - 1)
    for i in range(n - m + 1):
        product, sum = 1, 0
        for j in range(i, m + i):
            product = product * (ord(string[j]) - ord('0'))
            sum = sum + (ord(string[j]) - ord('0'))
        maxProd = max(maxProd, product)
        maxSum = max(maxSum, sum)
    print("Maximum Product =", maxProd)
    print("Maximum sum =", maxSum)


if __name__ == "__main__":
    string = "3605356297"
    m = 3
    maxProductSum(string, m)
