import math


def divisibleBy20(num):
    lastTwoDigits = int(num[-2:])
    return ((lastTwoDigits % 5 == 0 and lastTwoDigits % 4 == 0))


num = "63284689320"
if (divisibleBy20(num)):
    print("Yes")
else:
    print("No")
