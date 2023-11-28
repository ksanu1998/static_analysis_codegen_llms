def canConvert(str1, str2):
    i, j = 0, 0
    while (i < len(str1) and j < len(str2)):
        if (str1[i] != str2[j]):
            if (str1[i] == '0' and str2[j] == '1' and i +
                    1 < len(str1) and str1[i + 1] == '0'):
                i += 2
                j += 1
            else:
                return False
        else:
            i += 1
            j += 1
    if (i == len(str1) and j == len(str2)):
        return True
    return False


str1 = "00100"
str2 = "111"
if (canConvert(str1, str2)):
    print("Yes")
else:
    print("No")
