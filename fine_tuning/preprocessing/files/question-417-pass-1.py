def maxSum(tri, n):
    # Initialize the maximum sum
    max_sum = 0

    # Loop through each row of the triangle
    for row in range(n):
        # Get the elements of the current row
        row_elements = tri[row]

        # Initialize the sum for the current row
        row_sum = 0

        # Loop through each element of the current row
        for col in range(row+1):
            # Add the current element to the sum
            row_sum += row_elements[col]

            # Check if the sum is greater than the maximum sum
            if row_sum > max_sum:
                # Update the maximum sum
                max_sum = row_sum

    # Return the maximum sum
    return max_sum
