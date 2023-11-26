def maxSumBitonicSubArr(arr, n):
    # Initialize variables
    max_sum = 0
    curr_sum = 0

    # Iterate through the array
    for i in range(n):
        # Check if the current element is greater than the previous element
        if i > 0 and arr[i] > arr[i-1]:
            # Add the current element to the sum
            curr_sum += arr[i]
        else:
            # Reset the sum to 0
            curr_sum = 0

        # Update the maximum sum
        max_sum = max(max_sum, curr_sum)

    # Return the maximum sum
    return max_sum
