import sys



def findMissingNums(even, sizeEven, odd, sizeOdd):
    # Initialize two empty lists to store the missing even and odd numbers
    missingEven = []
    missingOdd = []

    # Iterate through the even numbers and check if they are in the range of 1 to sizeEven
    for num in even:
        if num not in range(1, sizeEven + 1):
            missingEven.append(num)

    # Iterate through the odd numbers and check if they are in the range of 1 to sizeOdd
    for num in odd:
        if num not in range(1, sizeOdd + 1):
            missingOdd.append(num)

    # Return the missing even and odd numbers
    return missingEven, missingOdd
