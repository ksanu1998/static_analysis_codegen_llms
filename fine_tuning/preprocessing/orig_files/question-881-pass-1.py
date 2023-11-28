def checkFibinnary(n):
    prev_last = 0
    while (n):
        if ((n & 1) and prev_last):
            return False
        prev_last = n & 1
        n >>= 1
    return True


n = 10
if (checkFibinnary(n)):
    print("YES")
else:
    print("NO")
