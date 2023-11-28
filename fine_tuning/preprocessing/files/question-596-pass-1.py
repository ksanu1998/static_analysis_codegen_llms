def isPrimeString(str1):
    if str1 == "":
        return True
    for i in range(2, int(str1) + 1):
        if str1 == str(i):
            return True
    return False
