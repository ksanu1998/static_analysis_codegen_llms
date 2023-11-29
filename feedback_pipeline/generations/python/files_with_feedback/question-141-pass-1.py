import sys
from math import sqrt


def min_moves(n):import sys
from math import sqrt

def min_moves(n):
    # Initialize variables
    min_moves = 0
    current = 1

    # Loop until we reach the target number
    while current!= n:
        # If the current number is even, we can move right
        if current % 2 == 0:
            current = current // 2
        # If the current number is odd, we can move down
        else:
            current = current * 3 + 1
        min_moves += 1

    return min_moves
