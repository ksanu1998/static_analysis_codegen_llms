def maxLenSubArr(a, n):

def maxLenSubArr(a, n):
    # Initialize the result
    max_len = 1
    curr_len = 1

    # Iterate through the array
    for i in range(1, n):
        # Check if the current element is equal to the previous element
        if a[i] == a[i-1]:
            # Increment the current length
            curr_len += 1
        else:
            # Check if the current length is greater than the max length
            if curr_len > max_len:
                max_len = curr_len

            # Reset the current length
            curr_len = 1

    # Check if the final length is greater than the max length
    if curr_len > max_len:
        max_len = curr_len

    return max_len
