NumUnsignBits = 64



def findNum(x):
    num = x
    while True:
        if num == int(num):
            return num
        num += 1
