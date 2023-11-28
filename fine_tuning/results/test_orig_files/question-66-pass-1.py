def Centered_Hexadecagonal_num(n):

def Centered_Hexadecagonal_num(n):
    num = 1
    for i in range(1, n+1):
        num += 6*i - 6
    return num
