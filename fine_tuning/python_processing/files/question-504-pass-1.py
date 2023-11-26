def isPalindrome(Str):
    # Remove all consecutive duplicates
    no_dup_str = "".join(Str.replace(Str[i], "") for i in range(len(Str)))
    # Check if string is a palindrome
    return no_dup_str == no_dup_str[::-1]
