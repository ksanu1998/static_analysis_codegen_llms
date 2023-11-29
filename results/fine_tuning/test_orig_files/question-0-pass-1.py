def maxPresum(a, b):

def maxPresum(a, b):
    # Initialize the maximum prefix sum to 0
    max_sum = 0
    # Loop through the elements of both arrays
    for i in range(len(a)):
        for j in range(len(b)):
            # Calculate the sum of the current elements
            current_sum = a[i] + b[j]
            # If the sum is greater than the maximum prefix sum, update it
            if current_sum > max_sum:
                max_sum = current_sum
    # Return the maximum prefix sum
    return max_sum
