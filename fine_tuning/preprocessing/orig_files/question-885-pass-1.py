import math


def isDvisibleBy12(num):
    if (len(num) >= 3):
        d1 = int(num[len(num) - 1])
        if (d1 % 2 != 0):
            return False
        d2 = int(num[len(num) - 2])
        sum = 0
        for i in range(0, len(num)):
            sum += int(num[i])
        return (sum % 3 == 0 and (d2 * 10 + d1) % 4 == 0)
    else:
        number = int(num)
        return (number % 12 == 0)


num = "12244824607284961224"
if (isDvisibleBy12(num)):
    print("Yes")
else:
    print("No")
