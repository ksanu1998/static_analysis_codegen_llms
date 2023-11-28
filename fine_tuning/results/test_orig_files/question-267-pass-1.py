from math import gcd, sqrt



def sumcommDiv(a, b):
    # Find the greatest common divisor of a and b
    g = gcd(a, b)

    # Initialize the sum to 0
    sum = 0

    # Iterate from 1 to the square root of the greatest common divisor
    for i in range(1, int(sqrt(g)) + 1):
        # If i is a common divisor of a and b, add it to the sum
        if (a % i == 0) and (b % i == 0):
            sum += i

    return sum
