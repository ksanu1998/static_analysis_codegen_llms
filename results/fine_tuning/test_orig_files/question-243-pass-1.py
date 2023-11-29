import math



def minAbsDiff(n):
    # Initialize the minimum absolute difference to infinity
    min_diff = float('inf')
    # Loop through the range of powers of 2
    for i in range(1, int(math.log2(n)) + 1):
        # Calculate the current power of 2
        power = 2 ** i
        # Calculate the absolute difference between n and the current power of 2
        diff = abs(n - power)
        # Update the minimum absolute difference if the current difference is less than the previous minimum
        if diff < min_diff:
            min_diff = diff
    # Return the minimum absolute difference
    return min_diff
