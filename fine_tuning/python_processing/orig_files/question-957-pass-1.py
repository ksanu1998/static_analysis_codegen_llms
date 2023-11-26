def nthPalindrome(n, k):
    if (k & 1):
        temp = k // 2
    else:
        temp = k // 2 - 1
    palindrome = 10 ** temp
    palindrome = palindrome + n - 1
    print(palindrome, end="")
    if (k & 1):
        palindrome = palindrome // 10
    while (palindrome):
        print(palindrome % 10, end="")
        palindrome = palindrome // 10


if __name__ == '__main__':
    n = 6
    k = 5
    print(n, "th palindrome of", k, " digit = ", end=" ")
    nthPalindrome(n, k)
    print()
    n = 10
    k = 6
    print(n, "th palindrome of", k, "digit = ", end=" ")
    nthPalindrome(n, k)
