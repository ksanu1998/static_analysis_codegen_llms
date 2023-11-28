def findNthNumber(N):

def findNthNumber(N):
    nth_number = 1
    for i in range(N-1):
        nth_number = str(int(nth_number))
        if len(nth_number) == 1:
            nth_number = "10" + nth_number
        else:
            nth_number = str(int(nth_number) + 1)
    return nth_number
