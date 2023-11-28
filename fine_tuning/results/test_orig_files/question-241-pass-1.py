def divide(a, b):

def divide(a, b):
    # Find the common divisors of a and b
    divisors = set(range(1, min(a, b) + 1)) & set(range(a, 0, -1)) & set(range(b, 0, -1))

    # Divide a and b by their common divisors
    result = []
    for divisor in divisors:
        result.append(a / divisor)
        result.append(b / divisor)

    return result[0], result[1]
