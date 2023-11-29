def digitSum(n):

def digitSum(n):
    # Initialize the sum to 0
    sum = 0
    # Loop through the digits of n
    for digit in str(n):
        # Add the digit to the sum
        sum += int(digit)
    # Return the sum
    return sum
