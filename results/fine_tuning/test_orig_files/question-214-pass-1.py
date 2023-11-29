def minSum(arr, n, x):

def minSum(arr, n, x):
    # Initialize the minimum sum to infinity
    min_sum = float("inf")
    # Loop through each element in the array
    for i in range(n):
        # Calculate the sum of the elements in the array that are greater than or equal to x
        sum_greater_than_x = sum(arr[i:])
        # Calculate the sum of the elements in the array that are less than x
        sum_less_than_x = sum(arr[:i])
        # Calculate the minimum sum
        min_sum = min(min_sum, abs(sum_greater_than_x - sum_less_than_x))
    # Return the minimum sum
    return min_sum
