def isSubSeqDivisible(st):
    l = len(st)
    arr = [int(ch)for ch in st]
    for i in range(0, l):
        for j in range(i, l):
            for k in range(j, l):
                if (arr[i] % 8 == 0):
                    return True
                elif ((arr[i] * 10 + arr[j]) % 8 == 0 and i != j):
                    return True
                elif ((arr[i] * 100 + arr[j] * 10 + arr[k]) % 8 == 0 and i != j and j != k and i != k):
                    return True
    return False


st = "3144"
if (isSubSeqDivisible(st)):
    print("Yes")
else:
    print("No")
