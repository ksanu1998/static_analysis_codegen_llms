def repeatedSum(n):
    sum_digits = 0
    product_digits = 1
    while len(str(n)) > 1:
        for digit in str(n):
            sum_digits += int(digit)
            product_digits *= int(digit)
        n = sum_digits
        sum_digits = 0
    return max(n, product_digits)
