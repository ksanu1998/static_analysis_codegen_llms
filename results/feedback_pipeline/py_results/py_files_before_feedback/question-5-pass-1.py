def sameProductQuadruples(nums, N):
    # Initialize a counter to store the number of quadruples
    count = 0

    # Loop over each number in the array
    for i in range(N):
        # Get the current number
        num1 = nums[i]

        # Loop over each remaining number in the array
        for j in range(i+1, N):
            # Get the second number
            num2 = nums[j]

            # Calculate the product of the two numbers
            prod = num1 * num2

            # Loop over each remaining number in the array
            for k in range(j+1, N):
                # Get the third number
                num3 = nums[k]

                # Calculate the product of the three numbers
                prod2 = prod * num3

                # Check if the product of the three numbers is equal to the product of the remaining pair
                if prod2 == nums[i] * nums[j]:
                    # Increment the counter by 1
                    count += 1

    # Return the number of quadruples
    return count