def minInt(str1):
    n = len(str1)
    if (n == 1):
        return (str1[0] - '0')
    if (n == 2):
        if (str1[0] == '1' and str1[1] == '0'):
            return 1
        if (str1[0] == '0' and str1[1] == '1'):
            return 1
        return 0
    if (n == 3):
        if (str1[0] == '1' and str1[1] == '1' and str1[2] == '0'):
            return 2
        if (str1[0] == '1' and str1[1] == '0' and str1[2] == '1'):
            return 2
        if (str1[0] == '0' and str1[1] == '1' and str1[2] == '1'):
            return 2
        if (str1[0] == '0' and str1[1] == '0' and str1[2] == '0'):
            return 0
        return 1
    if (n == 4):
        if (str1[0] == '1' and str1[1] == '1' and str1[2] == '1' and str1[3] == '0'):
            return 3
        if (str1[0] == '1' and str1[1] == '1' and str1[2] == '0' and str1[3] == '1'):
            return 3
        if (str1[0] == '1' and str1[1] == '0' and str1[2] == '1' and str1[3] == '1'):
            return 3
        if (str1[0
