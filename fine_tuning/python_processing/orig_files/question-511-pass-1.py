import math


def checkSuffix(A, B):
    digit_B = int(math .log10(B)) + 1
    A -= B
    return (A % int(math .pow(10, digit_B)))


A = 12345
B = 45
result = checkSuffix(A, B)
if (result == 0):
    print("Yes")
else:
    print("No")
