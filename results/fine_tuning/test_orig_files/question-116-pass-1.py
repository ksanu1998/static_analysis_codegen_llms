def findDistinctOddsumm(n, k):

def find_distinct_odd_summ(n, k):
    # Initialize a list to store the positive odd integers
    odd_ints = []
    # Initialize a variable to store the sum of the integers
    sum = 0
    # Loop through the range of positive odd integers
    for i in range(1, n+1, 2):
        # If the sum of the integers is less than the target sum
        if sum < n:
            # Add the current integer to the list of integers
            odd_ints.append(i)
            # Update the sum of the integers
            sum += i
        # If the sum of the integers is greater than or equal to the target sum
        else:
            # Break out of the loop
            break
    # Return the list of integers
    return odd_ints
