import sys
from math import sqrt



def min_moves(n):
    # Initialize the minimum number of moves to 0
    min_moves = 0

    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Calculate the distance between the current number and the target number
        distance = abs(i - n)

        # If the distance is greater than the minimum number of moves, break the loop
        if distance > min_moves:
            break

        # Add the distance to the minimum number of moves
        min_moves += distance

    return min_moves
