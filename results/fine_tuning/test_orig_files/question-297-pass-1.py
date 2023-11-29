def sumProductDifference(a, b, c, d, e):

def sumProductDifference(a, b, c, d, e):
    # Calculate the roots of the quartic equation:
    # x^4 + ax^3 + bx^2 + cx + d = 0
    # Using the quadratic formula:
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    x3 = (-c + (c**2 - 4*b*d)**0.5) / (2*b)
    x4 = (-c - (c**2 - 4*b*d)**0.5) / (2*b)

    # Calculate the sum of the roots:
    sum_of_roots = x1 + x2 + x3 + x4

    # Calculate the product of the roots:
    product_of_roots = x1 * x2 * x3 * x4

    # Calculate the absolute difference between the sum and product of the roots:
    absolute_difference = abs(sum_of_roots - product_of_roots)

    return absolute_difference
