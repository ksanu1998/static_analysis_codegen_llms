def calNum(year):

def calNum(year):
    count = 0
    for i in range(year):
        if i % 400 == 0 or (i % 4 == 0 and i % 100!= 0):
            count += 1
    return count
