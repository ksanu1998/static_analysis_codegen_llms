def solve(n):
    # Calculate the number of palindromic numbers with the given number of digits
    num_palindromes = 10 ** (n - 1)
    for i in range(n - 1):
        num_palindromes = num_palindromes * 9

    # Calculate the total number of possible numbers with the given number of digits
    total_nums = 10 ** n

    # Return the probability of a N digit number being a palindrome
    return num_palindromes / total_nums