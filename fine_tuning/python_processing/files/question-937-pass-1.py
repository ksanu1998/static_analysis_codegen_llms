def minNum(arr, n):
    # Calculate the sum of the array
    total = sum(arr)

    # Check if the sum is already even
    if total % 2 == 0:
        return 0

    # Initialize a variable to store the minimum number
    min_num = float('inf')

    # Iterate over the array
    for i in range(n):
        # Check if the number is less than the minimum number
        if arr[i] < min_num:
            # Update the minimum number
            min_num = arr[i]

    # Return the minimum number
    return min_num
