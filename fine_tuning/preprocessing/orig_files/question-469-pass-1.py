def findMissingDigit(a, b, c):
    w = 1
    a_mod_11 = 0
    for i in range(len(a) - 1, -1, -1):
        a_mod_11 = (a_mod_11 + w * (ord(a[i]) - ord('0'))) % 11
        w = w * -1
    b_mod_11 = 0
    w = 1
    for i in range(len(b) - 1, -1, -1):
        b_mod_11 = (b_mod_11 + w * (ord(b[i]) - ord('0'))) % 11
        w = w * -1
    c_mod_11 = 0
    xSignIsPositive = True
    w = 1
    for i in range(len(c) - 1, -1, -1):
        if (c[i] == 'x'):
            xSignIsPositive = (w == 1)
        else:
            c_mod_11 = (c_mod_11 + w * (ord(c[i]) - ord('0'))) % 11
        w = w * -1
    x = ((a_mod_11 * b_mod_11) - c_mod_11) % 11
    if (not xSignIsPositive):
        x = -x
    return (x % 11 + 11) % 11


A = "123456789"
B = "987654321"
C = "12193263111x635269"
print(findMissingDigit(A, B, C))
