def checkPalindrome(str):
    n = len(str)
    count = 0
    for i in range(0, int(n / 2)):
        if (str[i] != str[n - i - 1]):
            count = count + 1
    if (count <= 1):
        return True
    else:
        return False


str = "abccaa"
if (checkPalindrome(str)):
    print("Yes")
else:
    print("No")
