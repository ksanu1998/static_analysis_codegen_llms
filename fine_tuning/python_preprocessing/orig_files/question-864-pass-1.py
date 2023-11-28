def everMeet(x1, x2, v1, v2):
    if (x1 < x2 and v1 <= v2):
        return False
    if (x1 > x2 and v1 >= v2):
        return False
    if (x1 < x2):
        x1, x2 = x2, x1
        v1, v2 = v2, v1
    while (x1 >= x2):
        if (x1 == x2):
            return True
        x1 = x1 + v1
        x2 = x2 + v2
    return False


x1 = 5
v1 = 8
x2 = 4
v2 = 7
if (everMeet(x1, x2, v1, v2)):
    print("Yes")
else:
    print("No")
