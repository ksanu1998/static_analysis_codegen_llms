def countDigits(a, b):
    count = 0
    p = abs(a * b)
    if (p == 0):
        return 1


'
   while (p > 0):
        count = count + 1
        p = p // 10
    return count
a = 33
b = -24
print ("Number of digits = ", countDigits (a, b ))
