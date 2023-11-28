def isPrimeString(str1):
    len1 = len(str1)
    n = 0
    for i in range(len1):
        n += ord(str1[i])
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


str1 = "geekRam"
if (isPrimeString(str1)):
    print("Yes")
else:
    print("No")
