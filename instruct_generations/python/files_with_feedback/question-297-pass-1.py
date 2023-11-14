def sumProductDifference(a, b, c, d, e):
    # Calculate the roots of the quartic equation
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    # Calculate the sum of the roots
    sum_of_roots = r1 + r2

    # Calculate the product of the roots
    product_of_roots = r1 * r2

    # Calculate the absolute difference between the sum and product of the roots
    abs_diff = abs(sum_of_roots - product_of_roots)

    return abs_diff
