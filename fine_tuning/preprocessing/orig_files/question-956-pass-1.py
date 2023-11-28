import math


def reverseNum(n):
    rev = 0
    while (n):
        rem = n % 10
        rev = (rev * 10) + rem
        n = int(n / 10)
    return rev


def isPalindrom(num):
    return num == reverseNum(num)


def nthPalindrome(n, k):
    num = math .pow(10, k - 1)
    while (True):
        if (isPalindrom(num)):
            n -= 1
        if (not n):
            break
        num += 1
    return int(num)


n = 6
k = 5
print(n, "th palindrome of", k, "digit =", nthPalindrome(n, k))
n = 10
k = 6
print(n, "th palindrome of", k, "digit =", nthPalindrome(n, k))
