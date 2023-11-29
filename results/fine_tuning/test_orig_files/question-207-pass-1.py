def findNumber(n):

def findNumbers(n):
    # Initialize a list to store the numbers
    numbers = []

    # Loop through all possible pairs of numbers
    for i in range(1, n):
        for j in range(i+1, n):
            # Check if the sum of the two numbers is a perfect square
            if (i + j) ** 0.5 == int((i + j) ** 0.5):
                # If it is, add them to the list
                numbers.append(i)
                numbers.append(j)

    # Return the list of numbers
    return numbers
