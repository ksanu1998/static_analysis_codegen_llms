import sys
INT_MAX = sys .maxsize


def count_min_length(s):
    # Initialize the minimum length as the length of the input string
    min_length = len(s)
    # Loop through each substring of the input string
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Check if the substring is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # Update the minimum length if the current substring is shorter than the previous minimum length
                min_length = min(min_length, j-i)
    return min_length
