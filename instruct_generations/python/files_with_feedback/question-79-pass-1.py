import math

def isConcentrichexagonal(N):
    # Find the number of digits in N
    num_digits = len(str(N))

    # Find the sum of the digits in N
    sum_digits = sum([int(digit) for digit in str(N)])

    # Check if the number of digits is equal to the sum of the digits
    if num_digits == sum_digits:
        return True
    else:
        return False
