def largestNumber(n):

def largestNumber(n):
    digits = [int(digit) for digit in str(n)]
    odd_digits = [digit for digit in digits if digit % 2 == 1]
    if len(odd_digits) == 0:
        return -1
    largest_odd_digit = max(odd_digits)
    return int(str(largest_odd_digit) * len(digits))
