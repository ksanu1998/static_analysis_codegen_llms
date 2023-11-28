def floorDifference(A, N, X):
    # Calculate the sum of the array elements
    sum_of_array = sum(A)

    # Calculate the floor of the sum of the array elements divided by X
    floor_sum = sum_of_array // X

    # Calculate the absolute difference between the floor of the sum and the sum of every array element divided by X
    abs_diff = abs(floor_sum - sum_of_array // X)

    return abs_diff
