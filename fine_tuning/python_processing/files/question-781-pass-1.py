def maxModProdSubarr(arr, n, M):
    # Initialize variables
    max_prod = 1
    curr_prod = 1

    # Iterate through the array
    for i in range(n):
        # Update the maximum product
        max_prod = max(max_prod, curr_prod)

        # Update the current product
        curr_prod *= arr[i]

        # Check if the current product is greater than the modulus
        if curr_prod >= M:
            # If so, update the current product to be the remainder of dividing it by the modulus
            curr_prod %= M

    # Return the maximum product
    return max_prod
