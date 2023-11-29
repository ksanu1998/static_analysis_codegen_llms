def getMaxNum(a, b, c):

def getMaxNum(a, b, c):
    max_num = 0
    for i in range(a, b+1):
        if i % c == 0 and i > max_num:
            max_num = i
    return max_num
