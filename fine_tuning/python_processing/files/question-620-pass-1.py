def sentencePalindrome(s):
    # Remove all spaces and punctuation from the sentence
    s = s.replace(" ", "").replace(".", "").lower()
    # Check if the sentence is a palindrome
    return s == s[::-1]
