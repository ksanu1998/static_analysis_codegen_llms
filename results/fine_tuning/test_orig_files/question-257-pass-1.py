from math import ceil, floor



def sum(N, X, Y):
    sum = 0
    for i in range(N):
        if i % X == 0 or i % Y == 0:
            sum += i
    return sum
