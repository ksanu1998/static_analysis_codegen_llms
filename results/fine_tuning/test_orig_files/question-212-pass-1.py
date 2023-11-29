def findMinSum(arr, n):

def findMinSum(arr, n):
    # Initialize the result variable
    min_sum = 0

    # Iterate through the array and calculate the minimum sum of all subarrays
    for i in range(n):
        min_sum += arr[i]

    return min_sum
