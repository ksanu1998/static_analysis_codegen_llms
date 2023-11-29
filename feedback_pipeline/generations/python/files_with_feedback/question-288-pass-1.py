import sys


def CalculateDifference(arr, n):import sys

def calculate_difference(arr, n):
    # Calculate the sum of the array
    sum_of_arr = sum(arr)

    # Calculate the sum of the numbers from 1 to n
    sum_of_range = (n * (n + 1)) // 2

    # Calculate the absolute difference between the two sums
    abs_diff = abs(sum_of_arr - sum_of_range)

    return abs_diff
