from collections import defaultdict


def getPalindrome(st):
    # Create a dictionary to store the frequency of each character
    char_freq = defaultdict(int)
    for char in st:
        char_freq[char] += 1

    # Sort the characters based on their frequency
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Rearrange the characters to form a palindrome
    palindrome = ""
    for char, freq in sorted_chars:
        palindrome += char * (freq // 2)
        if freq % 2 == 1:
            palindrome += char

    return palindrome
