def maxSum(a, n):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    count = 0

    # Iterate through the array
    for i in range(n):
        current_sum += a[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
            count += 1
            if count > 2:
                break

    return max_sum
