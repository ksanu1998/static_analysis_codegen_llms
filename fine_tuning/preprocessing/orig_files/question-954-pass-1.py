def check(st):
    n = len(st)
    if (((int)(st[n - 1]) % 2) != 0):
        return False
    digitSum = 0
    for i in range(0, n):
        digitSum = digitSum + (int)(st[i])
    return (digitSum % 3 == 0)


st = "1332"
if (check(st)):
    print("Yes")
else:
    print("No ")
