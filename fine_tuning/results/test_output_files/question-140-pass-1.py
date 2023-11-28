def reverse(num):
    rev = 0
    while (num > 0):
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev


def findPalindrome(n):
    for i in range(1, n + 1):
        if (i == reverse(i)):
            print(i, end=" ")


if __name__ == "__main__":
    findPalindrome(3)
