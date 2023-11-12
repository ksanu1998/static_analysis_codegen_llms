import sys


def findMissingNums(even, sizeEven, odd, sizeOdd):# Create a dictionary to store the missing even numbers
    missingEvens = {}

    # Iterate over the even numbers and check if they are in the given array
    for i in range(sizeEven):
        if even[i] not in odd:
            missingEvens[even[i]] = True

    # Create a dictionary to store the missing odd numbers
    missingOdds = {}

    # Iterate over the odd numbers and check if they are in the given array
    for i in range(sizeOdd):
        if odd[i] not in even:
            missingOdds[odd[i]] = True

    # Return the union of the missing even and odd numbers
    return missingEvens.keys() + missingOdds.keys()


# Test the function with the following inputs and outputs:
print(findMissingNums([1, 2, 3, 4, 5], 5, [2, 4, 6], 3))  # [1, 3, 5, 6]
print(findMissingNums([2, 4, 6], 3, [1, 2, 3, 4, 5], 5))  # [6, 1, 5]
print(findMissingNums([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], 5))  # []
print(findMissingNums([1, 3, 5, 7, 9], 5, [2, 4, 6, 8, 10], 5))  # [2, 6, 10]
print(findMissingNums([2, 4, 6, 8, 10