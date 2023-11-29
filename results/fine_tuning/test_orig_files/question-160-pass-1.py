def solve(n):

def solve(n):
    # Calculate the number of digits in the palindrome
    num_digits = 10 ** n

    # Calculate the number of palindromes
    num_palindromes = 0
    for i in range(1, num_digits + 1):
        if str(i) == str(i)[::-1]:
            num_palindromes += 1

    # Return the probability
    return num_palindromes / num_digits
