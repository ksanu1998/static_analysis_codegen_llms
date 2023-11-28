import sys


def findMin(a, n):
    # Initialize the minimum difference to infinity
    min_diff = float("inf")
    # Loop through all possible partitions
    for i in range(1 << n):
        # Create two empty lists to store the elements of the two subsets
        subset1 = []
        subset2 = []
        # Loop through all elements of the set
        for j in range(n):
            # If the jth bit of i is set, add the element to the first subset
            # Otherwise, add it to the second subset
            if i & (1 << j):
                subset1.append(a[j])
            else:
                subset2.append(a[j])
        # Calculate the sum of the two subsets
        subset1_sum = sum(subset1)
        subset2_sum = sum(subset2)
        # Calculate the difference of the two sums
        diff = abs(subset1_sum - subset2_sum)
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff
