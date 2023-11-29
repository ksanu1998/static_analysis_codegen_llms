def findNumber(n):

def findNumber(n):
    for i in range(1, n+1):
        if str(i).count(str(n)) == 1:
            return i
    return -1
