def sumDigitSquare(n):
    sq = 0
    while (n):
        digit = n % 10
        sq = sq + digit * digit
        n = n // 10
    return sq


def isHappy(n):
    while (1):
        if (n == 1):
            return True
        n = sumDigitSquare(n)
        if (n == 4):
            return False
    return False


n = 23
if (isHappy(n)):
    print("Yes")
else:
    print("No")
