import sys

def minMoves(n):
    count = 0
    while n % 25!= 0:
        n += 1
        count += 1
    return count
