def find_numbers(n):
    # Initialize a list to store the numbers
    numbers = []

    # Loop through all possible pairs of numbers
    for i in range(1, n+1):
        for j in range(i, n+1):
            # Check if the sum of the two numbers is a perfect square
            if (i + j) ** 0.5 == int((i + j) ** 0.5):
                # If it is, add them to the list
                numbers.append((i, j))

    return numbers