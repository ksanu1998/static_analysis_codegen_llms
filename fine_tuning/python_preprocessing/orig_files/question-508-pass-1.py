def power(base, pwr):
    res = 1
    while (pwr > 0):
        if (pwr & 1):
            res = res * base
        base = base * base
        pwr >>= 1
    return res


def countNonPalindromicString(n, m):
    total = power(n, m)
    palindrome = power(n, m // 2 + m % 2)
    count = total - palindrome
    return count


if __name__ == '__main__':
    n = 3
    m = 5
    print(countNonPalindromicString(n, m))
