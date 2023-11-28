import math


def findMaxGCD(arr, n, k):
    # Initialize result
    result = 1

    # Loop through all subarrays of size k
    for i in range(n - k + 1):
        # Find the maximum GCD of the subarray
        gcd = math.gcd(max(arr[i:i+k]), result)
        # Update the result if the maximum GCD is greater than the current result
        if gcd > result:
            result = gcd

    # Return the result
    return result
