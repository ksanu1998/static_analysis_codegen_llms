import sys



def closetAND(arr, n, k):
    # Initialize result as -1
    result = -1

    # Loop through all possible values of k
    for i in range(n):
        # Calculate the bitwise AND of the current element and the previous element
        current_and = arr[i] & arr[i-1]

        # If the bitwise AND is equal to k, we have found the closest value to k
        if current_and == k:
            result = arr[i]
            break

    return result
