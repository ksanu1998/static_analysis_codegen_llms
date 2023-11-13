def find_distinct_odd_summ(n, k):
    # Initialize a list to store the first k odd integers
    # that sum up to n
    result = []

    # Initialize two variables to keep track of the current
    # number and its sum
    num = 1
    sum = 0

    # Loop until we have found k distinct positive odd integers
    # that sum up to n
    while len(result) < k:
        # If the sum is less than n, add the current number
        # to the result list and increment the sum
        if sum < n:
            result.append(num)
            sum += num
            num += 2
        # If the sum is greater than n, decrement the current
        # number and subtract it from the sum
        else:
            result.pop()
            sum -= num
            num -= 2

    return result