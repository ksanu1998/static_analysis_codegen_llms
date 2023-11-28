def printIndex(str, s):
    flag = False
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):
            print(i, end=" ")
            flag = True
    if (flag == False):
        print("NONE")


str1 = "GeeksforGeeks"
str2 = "Geeks"
printIndex(str1, str2)
