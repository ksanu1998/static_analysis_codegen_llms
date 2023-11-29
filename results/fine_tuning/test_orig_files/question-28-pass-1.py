def maxLCMWithGivenSum(X):

def maxLCMWithGivenSum(X):
    # Initialize the maximum LCM as 1
    max_lcm = 1

    # Initialize the sum as X
    sum = X

    # Loop through all positive integers
    for i in range(1, X + 1):
        # If the sum is equal to the current number, return the current number and X
        if sum == i:
            return i, X

        # If the sum is greater than the current number, add the current number to the sum and continue the loop
        elif sum > i:
            sum += i

        # If the sum is less than the current number, subtract the current number from the sum and continue the loop
        else:
            sum -= i

    # If the loop completes and no numbers are found, return None
    return None
