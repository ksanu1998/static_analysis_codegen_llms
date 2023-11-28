def isValidNesbitt(a, b, c):
    A = a / (b + c)
    B = b / (a + c)
    C = c / (a + b)
    inequality = A + B + C
    return (inequality >= 1.5)


a = 1.0
b = 2.0
c = 3.0
if (isValidNesbitt(a, b, c)):
    print(
        "Nesbitt's inequality satisfied.",
        " for real numbers ",
        a,
        ", ",
        b,
        ", ",
        c)
else:
    print("Not satisfied")
