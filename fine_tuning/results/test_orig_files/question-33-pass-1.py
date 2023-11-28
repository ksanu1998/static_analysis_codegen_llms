def print_h_index(arr, N):

def print_h_index(arr, N):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result array
    result = [0] * N
    # Iterate through the array and calculate the h-index for each element
    for i in range(N):
        # Calculate the number of elements with greater or equal frequencies
        count = 0
        for j in range(i, N):
            if arr[j] >= i + 1:
                count += 1
        # Assign the h-index to the current element
        result[i] = count
    return result
