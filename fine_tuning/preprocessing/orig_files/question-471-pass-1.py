def isPossible(str1, str2):
    arr = {}
    l1 = len(str1)
    l2 = len(str2)
    possible = True
    for i in range(l1):
        arr[str1[i]] = 1
    for i in range(l2):
        if str2[i] != ' ':
            if arr[str2[i]] == 1:
                continue
            else:
                possible = False
                break
    if possible:
        print("Yes")
    else:
        print("No")


str1 = "we all love geeksforgeeks"
str2 = "we all love geeks"
isPossible(str1, str2)
