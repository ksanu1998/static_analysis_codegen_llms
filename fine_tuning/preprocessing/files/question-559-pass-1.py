def isPalindrome(s, i, j):
    return s[i:j+1] == s[i:j+1][::-1]
