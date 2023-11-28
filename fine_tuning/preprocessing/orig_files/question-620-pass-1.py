def sentencePalindrome(s):
    l, h = 0, len(s) - 1
    s = s .lower()
    while (l <= h):
        if (not (s[l] >= 'a' and s[l] <= 'z')):
            l += 1
        elif (not (s[h] >= 'a' and s[h] <= 'z')):
            h -= 1
        elif (s[l] == s[h]):
            l += 1
            h -= 1
        else:
            return False
    return True


s = "Too hot to hoot."
if (sentencePalindrome(s)):
    print "Sentence is palindrome."
else:
    print "Sentence is not palindrome."
