def product_subarrays(arr, n):
    # Initialize the result array with all 1s
    result = [1] * n

    # Compute the product of all elements in the array
    # and store it in the result array
    prod = 1
    for i in range(n):
        prod *= arr[i]
        result[i] *= prod

    # Compute the product of all elements from the end
    # and store it in the result array
    inv_prod = 1
    for i in range(n-1, -1, -1):
        inv_prod *= arr[i]
        result[i] *= inv_prod

    return result