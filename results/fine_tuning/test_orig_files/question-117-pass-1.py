def checkArray(a, b, n):

def checkArray(a, b, n):
    # Initialize the result variable
    result = 0

    # Iterate through the arrays and compare the elements
    for i in range(n):
        if a[i]!= b[i]:
            # If the elements are not equal, increment the result variable
            result += 1

    # Return the result
    return result
