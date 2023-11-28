import sys


def CalculateDifference(arr, n):

def calculate_difference(arr, n):
    # Calculate the sum of the array
    sum_of_array = sum(arr)

    # Calculate the sum of the first n elements of the array
    sum_of_first_n = sum(arr[:n])

    # Calculate the absolute difference between the two sums
    absolute_difference = abs(sum_of_array - sum_of_first_n)

    return absolute_difference
