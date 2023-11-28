def isEven(arr, n, r):

def isEven(arr, n, r):
    # Initialize result as 0
    result = 0

    # Iterate through the array
    for i in range(n):
        # If the current digit is 0, result is 0
        if arr[i] == 0:
            result = 0
        # If the current digit is 1, result is 1
        elif arr[i] == 1:
            result = 1
        # If the current digit is any other number, result is -1
        else:
            result = -1

    # Return the result
    return result
