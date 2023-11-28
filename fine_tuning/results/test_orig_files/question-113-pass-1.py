def product_subarrays(arr, n):

def product_subarrays(arr, n):
    # Initialize the result array with all 1s
    result = [1] * n

    # Initialize the product variable
    product = 1

    # Iterate over the array
    for i in range(n):
        # Update the product variable
        product *= arr[i]

        # Update the result array
        result[i] = product

    # Initialize the product variable
    product = 1

    # Iterate over the array in reverse
    for i in range(n-1, -1, -1):
        # Update the product variable
        product *= arr[i]

        # Update the result array
        result[i] *= product

    # Return the result array
    return result
