def totalways(arr, n):

def totalways(arr, n):
    # Initialize the result variable
    result = 0

    # Loop through the array
    for i in range(n):
        # Calculate the absolute difference between the current element and the element on its right
        diff = abs(arr[i] - arr[i+1])

        # Increment the result variable by the absolute difference
        result += diff

    # Return the result
    return result
