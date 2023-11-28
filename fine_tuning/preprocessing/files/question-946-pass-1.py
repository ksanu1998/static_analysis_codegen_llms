def printEqualModNumbers(arr, n):
    # Initialize the value of k
    k = arr[0]

    # Loop through the array and find the first number that is not equal to k
    for i in range(1, n):
        if arr[i]!= k:
            break

    # If k is not equal to any of the array elements, return -1
    if i == n:
        return -1

    # Return the first number that is not equal to k
    return arr[i]
