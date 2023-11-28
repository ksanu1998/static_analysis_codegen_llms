def returnWinner(s, l):
    # Initialize a list to store the palindromes
    palindromes = []

    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the character is a palindrome
        if s[i:i+l] == s[i:i+l][::-1]:
            # If it is, add it to the list of palindromes
            palindromes.append(s[i:i+l])

    # Check if there are any palindromes in the list
    if palindromes:
        # If there are, return the first one
        return palindromes[0]
    else:
        # If there aren't, return None
        return None
