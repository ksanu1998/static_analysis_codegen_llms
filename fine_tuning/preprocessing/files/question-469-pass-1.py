def findMissingDigit(a, b, c):
    product = a * b * c
    digits = [int(digit) for digit in str(product)]
    missing_digit = max(digits) + 1
    while missing_digit in digits:
        missing_digit += 1
    return missing_digit
