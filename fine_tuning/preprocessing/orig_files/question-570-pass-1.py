def matchPattern(s):
    count = 0
    n = len(s)
    i = 0
    while (i < n):
        while (i < n and s[i] == 'a'):
            count += 1
            i = +1
        while (i < n and s[i] == 'b'):
            count -= 1
            i += 1
        if (count != 0):
            return False
    return True


s = "bb"
if (matchPattern(s)):
    print("Yes")
else:
    print("No")
