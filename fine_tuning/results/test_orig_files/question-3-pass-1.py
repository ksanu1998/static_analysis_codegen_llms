def findNthNumber(N):

def findNthNumber(N):
    n = 1
    while True:
        if str(n).count("9") == 0:
            if n == N:
                return n
            else:
                n += 1
        else:
            n += 1
