def getResult(n):
    digits = [int(digit) for digit in str(n)]
    even_digits = digits[::2]
    odd_digits = digits[1::2]
    if even_digits == odd_digits:
        return True
    else:
        return False
