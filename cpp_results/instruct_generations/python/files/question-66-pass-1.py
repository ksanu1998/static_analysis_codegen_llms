def Centered_Hexadecagonal_num(n):
    num = 1
    for i in range(1, n+1):
        num += 2*i - 1
    return num