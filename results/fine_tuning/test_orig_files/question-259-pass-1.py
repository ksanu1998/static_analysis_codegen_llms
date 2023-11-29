def getNumber(s):

def getNumber(s):
    # Initialize variables
    max_number = 0
    factorial_product = 1

    # Loop through the digits of the input number
    for digit in str(s):
        # Calculate the factorial of the current digit
        factorial = 1
        for i in range(1, int(digit) + 1):
            factorial *= i

        # Update the factorial product
        factorial_product *= factorial

        # Check if the current digit is the maximum number of digits
        if len(str(s)) == len(str(factorial_product)):
            max_number = s
            break

    return max_number
