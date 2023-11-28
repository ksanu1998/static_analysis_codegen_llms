import sys


def maxProductSum(string, m):
    # Initialize variables
    max_sum = 0
    max_product = 1

    # Iterate over the digits of the string
    for i in range(len(string)):
        # Calculate the product of the first m digits
        product = 1
        for j in range(i, i + m):
            product *= int(string[j])

        # Calculate the sum of the first m digits
        sum = 0
        for j in range(i, i + m):
            sum += int(string[j])

        # Update the maximum sum and product
        if sum > max_sum:
            max_sum = sum
        if product > max_product:
            max_product = product

    return (max_sum, max_product)
