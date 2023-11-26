def arrange(s):
    # Convert the binary string to a list of integers
    nums = [int(i) for i in s]

    # Sort the list in descending order
    nums.sort(reverse=True)

    # Return the first element of the list
    return nums[0]
