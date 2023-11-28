def precisionCompute(x, y, n):
    if y == 0:
        print("Infinite")
        return
    if x == 0:
        print(0)
        return
    if n <= 0:
        print(x / y)
        return
    if (((x > 0) and (y < 0)) or ((x < 0) and (y > 0))):
        print("-", end="")
        if x < 0:
            x = -x
        if y < 0:
            y = -y
    d = x / y
    for i in range(0, n + 1):
        print(d)
        x = x - (y * d)
        if x == 0:
            break
        x = x * 10
        d = x / y
        if (i == 0):
            print(".", end="")


x = 22
y = 7
n = 15
precisionCompute(x, y, n)
