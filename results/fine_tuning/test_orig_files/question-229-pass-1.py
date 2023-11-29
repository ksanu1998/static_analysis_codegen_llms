def getMinNum(a, b, c):

def getMinNum(a, b, c):
    min_num = 1
    while min_num % c!= 0 or min_num < a or min_num > b:
        min_num += 1
    return min_num
